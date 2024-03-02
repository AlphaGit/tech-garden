---
title: LLM Speed Performance
tags:
  - performance
  - llm
  - nlp
  - pytorch
  - gpus
  - links
enableToc: true
---
## Performance concepts

- **Time to first token**: how long the model takes to generate the first token of the prediction, which is the lower bound on the time a user has to wait to see anything from the response.
- **Latency:** how long the model takes to generate the next token in the prediction. A latency slower than the human reading speed will be perceived as "slow", as the application cannot generate a response faster than the user can read it.
- **Throughput:** how many distinct generations can we pass through the pipeline at once.
- **Hardware Utilization:** how efficiently are we using the compute, memory bandwidth, and other capabilities of the hardware.

## LLMs related concepts

- **Transformers are Auto-regressive:** LLMs work on auto-regressive algorithms, meaning that the algorithm has to process an increasing number of tokens every cycle, and in each cycle we add another token to the context to be processed. That means to generate 100 tokens from a 10 token prompt, you don't need to run model on only 109 tokens. You need to run it on 10 + 11 + 12 + 13 + ... + 109 = 5,950 tokens!
## Performance considerations 
### 1. Reduce the roundtrips between CPU-GPU

#### 1.1. Use  `torch.compile`

Use `torch.compile(decoding_fn, mode="reduce-overhead", fullgraph=True)`. This will send the full [[CUDAGraph]] to the GPU with pre-compiled instructions. It is a quick way to get better performance out of the hardware without dipping down to CUDA to write kernels.

#### 1.2. Increase the batch size

Increasing the batch size will move the problem to be closer to a CPU-bound problem rather than a memory-bound problem.

However, a batch size too big will result in the GPU being out of memory to calculate inference. Consider that the GPU needs space both for the KV-Cache and the model parameters. This note also applies to the sequence length to be inferred.

Increasing the batch size will improve the throughput of the model and uses the hardware more efficiently, but it could increase the time to first token, and the generation latency.
### 2. Batch model generations

> To batch generation, we pass the model multiple sequences at once, generating a completion for each in the same forward pass. This requires the sequences to be padded on either the left or right with filler tokens to equal length. The padding tokens are masked in the attention mask so that they don't influence generation.

This will improve the throughput and improve the use of the hardware but might increase the time to first token.
### 3. Improve performance of the KV-Cache

#### 3.1. Setup a bigger cache for the pre-fill of the KV-Cache

> KV caching helps with the algorithmic side of LLM slowness—since we're now only passing in a single token on each step, we don't have to redo _everything_ for each new token. However, it doesn't completely banish the problem, since the KV cache still grows in size each step, slowing down the attention calculation. The size of the KV cache can also pose its own, new problem—for example, with a 1,000 token KV cache, even with the smallest GPT-2 there are 18,432,000 values being cached. If each is an fp32, that's almost 74MB of cache, for a single generation, for a comparatively tiny model! (LLMFast)

```python
with torch.device(device):
	model.setup_caches(match_batch_size=1, max_seq_length=max_seq_length)

# Re-compile the decoding function to accomodate for a dynamic cache
# This replaces the previous step
decode_one_token = torch.compile(
	decode_one_token,
	mode="reduce-overhead",
	fullgraph=True
)
prefill = torch.compile(
	prefill,
	dynamic=True,
	fullgraph=True
) 
```

#### 3.2. Alternatively, use a static cache

```python
from transformers import AutoModelForCausalLM, StaticCache
device = "cuda"

...

model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf", torch_dtype=torch.bfloat16)
model = model.to(device).eval()

...

model._setup_cache(StaticCache, batch_size, max_cache_len=max_cache_length)
```
[^static_kv_cache]
### 4. Improve the attention mechanism

The attention mechanism (that picks the right token based on the changing context) is also a quadratic algorithm. All tokens attend to all tokens, leading to $N^2$ scaling.
#### 3.1. Use vLLM or paged attention

Both these techniques work as a middle-step between the memory available and the memory required. It's very similar to another level of memory where chunks of it are loaded in the device while the rest of it is paged and kept in a lower level.

[[vLLM]]

#### 3.2. FlashAttention

Instead of storing the full attention matrix in the HBM, do block-wise computation of the dot product, such that all the computation is performed in the L2 cache.

If writing the model manually, you can replace the attention mechanism:

```python
F.softmax(q @ k.T / sqrt(k.size(-1)) + mask) @ v
```

for:

```python
torch.nn.functional.scaled_dot_product_attention
```

which will delegate to [[Flash Attention]] if available.

#### 3.3. Multi-query attention

> Multi-Query attention is a change to the model architecture that shrinks the size of the KV cache by assigning multiple heads to $Q$, and only a single head to $K$ and $V$. It needs to be trained into the model from the beginning—it's not just an inference-time optimization—but it's worth being aware of if you're trying to choose a model, because models with MQA can support more tokens in the KV cache than models trained with normal attention. (LLMFast)

> So what is [Multi-Query Attention](https://arxiv.org/abs/1911.02150)? Instead of Q, K, and V all being split into separate heads, _only_ Q is split. \[...] You might think this would be a serious problem for the model, but it actually has only a small effect on perplexity. (LLMFast)


#### 3.4. Grouped-query attention

> Mistral 7B uses a variant called [Grouped-Query Attention](https://arxiv.org/abs/2305.13245v2) which is a hybrid between MQA and MHA. If MHA is `Q_heads=K_heads=V_heads=N` and MQA is `Q_heads=N; K_heads=V_heads=1`, then GQA is `Q_heads=N; K_heads=V_heads=G` where `1 < G < N`. GQA claims less effect on perplexity and better training stability than MQA. (LLMFast)


#### 3.5. Sparse Attention

> Attention is algorithmically slow because it's quadratic: as the sequence grows in length, each of the N tokens needs to attend to each of the N tokens. Sparse attention attempts to remedy this by calculating less attention.
> 
> For example, Mistral 7B uses sliding window attention, where tokens in some layers can only attend to nearby tokens. [Longformer](https://arxiv.org/abs/2004.05150) also explored some interesting sparse attention patterns, like giving all tokens access to specific positions, dilating the sliding window, using different size windows on different layers, and other tricks. (LLMFast)
### 5. Quantize the weights

Most of the models are set up with `fp32` (float32), so going down to `fp16` or half precision, will give you 50% savings. [[bfloat16]] ("brain float 16") developed by Google Brain, has better range but worse hardware support.

> When reducing the fields of a fp32, fp16 and bfloat16 made different tradeoffs: fp16 tried to balance between range and precision by shrinking both the exponent and fraction fields, whereas bfloat16 preserved the range of fp32 by keeping an 8-bit exponent, while sacrificing precision by shrinking the fraction field smaller than fp16. [The loss of range can sometimes be a problem for training in fp16](https://x.com/sytelus/status/1713462678226968973), but for inference either works, and fp16 is probably a better choice if your GPU doesn't support bfloat16. (LLMFast)

Consider quantizing down the weights to `int8`. This, in part, reduces the space required to load the model in memory. It also might come with extra benefits on the speed of the operations.

Note that further quantizing does not equal better speed, there is a trade-off for each model, so find out which is your case.

> [bitsandbytes](https://github.com/TimDettmers/bitsandbytes) also implements quantization for non-llama.cpp projects (LLMFast)

> However, it's also possible to finetune or train models with datatypes smaller than fp16. For example, you can train quantized low rank adapters with [qLoRA](https://github.com/artidoro/qlora), and [a 2022 paper](https://arxiv.org/abs/2209.05433) demonstrated training 175B parameter language models in (simulated) fp8, achieving very similar results to fp16. (LLMFast)
### 6. Use speculative-decoding

Unfortunately, this requires a second model, but the good news is that it might not be terribly complex as it can be derived from the first model.

Since some tokens are going to be highly probable after previous tokens (say, "going → going to"), we can use a smaller, simpler model to predict and generate those tokens. Once we run the bigger model, we can add the predicted token to the context, and use the bigger model to both confirm that the prediction was correct and get the token after it. In the best case, we've saved the generation of one of the tokens. In the worst case, we predicted wrong and just need to throw it away.

This can be done at multiple levels, where the second model ("draft" model, opposed to the original "oracle" model) has its tokens also predicted by another, yet simpler model.

Speculative decoding can be very-context dependent.
#### 6.1. Threshold decoding

> An approach I came up with to mitigate the issues with using a fixed number of draft tokens is _threshold decoding_.
>
> Instead of always decoding up to the maximum number of draft tokens, we keep a moving probability threshold, calibrated based on how many tokens are being accepted right now. Draft tokens are generated until the cumulative probability of the draft so far (based on the draft model logits) falls below this threshold. (LLMFast)

#### 6.2. Staged speculative decoding

> [Staged speculative decoding](https://arxiv.org/abs/2308.04623) adds two improvements to vanilla speculative decoding:
>
> The first is to restructure the draft batch as a tree, instead of a single generation. This helps because longer draft batches on complex text can quickly diverge from the base model. It can instead make more sense to do multiple, shorter drafts, branching off from each other, and then verify them all against the oracle model using a specially-crafted attention mask. Generating multiple draft sequences lets you reuse prior tokens and sample the draft model in batches, further accelerating the process.
> 
> The second improvement is to speculatively decode the draft model as well—it's usually a Transformer after all. This could be a yet-smaller Transformer (they recommend 15-20x smaller than the oracle model), or even a simple N-gram model.

#### 6.3. Lookahead decoding

> [Lookahead decoding](https://lmsys.org/blog/2023-11-21-lookahead-decoding/) is a new approach to speculative decoding that doesn't require a draft model. Instead, the model itself is used in two branches: a lookahead branch, which predicts and extends candidate N-grams (short sequences of N tokens), and a verification branch, which verifies the candidates. The lookahead branch is similar to the draft model in regular speculative decoding, and the verification branch has the same role as the oracle model.
>
> But unlike regular speculative decoding, this is all done not just in a single model, but in a single model _call_ using a specially-crafted attention mask. (LLMFast)
#### 6.4. Prompt lookup decoding

> [Prompt lookup decoding](https://twitter.com/apoorv_umang/status/1728831397153104255) is another technique, where the draft model is replaced by simple string matching over the context. They claim it works well for tasks like code editing or RAG where the output necessarily contains lots of verbatim copying from the input.
### 7. Guided generation

If we've got a request where we know what the grammar of the response is going to be (for example, generate JSON Output), we don't need the original model to generate all the tokens for the grammar itself. Instead, we can traverse the grammar an have the model generate the tokens for which we need inference.

> Even better, with libraries like [Outlines](https://github.com/outlines-dev/outlines) or [jsonformer](https://github.com/1rgs/jsonformer), you can give the guided generation sampler a schema, and it will sample _within that schema_! (LLMFast)

### 8. [[GPTQ]]

Post-training (further) quantization

- [AutoGPTQ](https://github.com/PanQiWei/AutoGPTQ), an LLM quantization package using [[ai/GPTQ|GPTQ]].
- [GPTQ for LLaMa](https://github.com/qwopqwop200/GPTQ-for-LLaMa) , a 4-bit quantization of [[LLaMA]] using [[ai/GPTQ|GPTQ]]

### 9. Apply tensor-paralellism

Running the code in multiple devices at the same time will accelerate the inference, at the expense of cost.

Some of results of these examples can be seen at https://github.com/pytorch-labs/gpt-fast

## 10. Try a rewritten/optimized model

There are a few alternatives that claim to be more optimized and faster for inference.

- [ExLlama](https://github.com/turboderp/exllama) as a replacement for [[LLaMA 2]], which uses 4-bit GPTQ weights.
- [ExLlama v2](https://github.com/turboderp/exllamav2), similar but followup to v1
## Sources

- [Accelerating Generative AI with PyTorch II: GPT, Fast](https://pytorch.org/blog/accelerating-generative-ai-2/), PyTorch blog
- [Towards 100x Speedup: Full Stack Transformer Inference Optimization](https://yaofu.notion.site/Towards-100x-Speedup-Full-Stack-Transformer-Inference-Optimization-43124c3688e14cffaf2f1d6cbdf26c6c), Yao Fu
- [vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention](https://blog.vllm.ai/2023/06/20/vllm.html), vLLM Team
- Chen, Carol. "Transformer Inference Arithmetic", https://kipp.ly/blog/transformer-inference-arithmetic/, 2022.
- [Extensive LLama.cpp benchmark & more speed on CPU, 7b to 30b, Q2_K, to Q6_K and FP16, X3D, DDR-4000 and DDR-6000](https://www.reddit.com/r/LocalLLaMA/comments/14ilo0t/extensive_llamacpp_benchmark_more_speed_on_cpu_7b/), from  u/Chromix\_ in r/LocalLLaMA, 2023-06-25.
- LLMFast: [How to make LLMs go fast](https://vgel.me/posts/faster-inference/), Theia @ vgel.me

[^static_kv_cache]: [
ArthurZucker/static_kv_cache.py](https://gist.github.com/ArthurZucker/af34221def212259b43d55a2811d2dbb)