---
title: LLM Speed Performance
tags:
  - performance
  - llm
  - nlp
  - pytorch
  - gpus
  - links
---
## Performance concepts

- **Time to first token**: how long the model takes to generate the first token of the prediction, which is the lower bound on the time a user has to wait to see anything from the response.
- **Latency:** how long the model takes to generate the next token in the prediction. A latency slower than the human reading speed will be perceived as "slow", as the application cannot generate a response faster than the user can read it.

## Performance considerations 
### 1. Reduce the roundtrips between CPU-GPU

#### 1.1. Use  `torch.compile`

Use `torch.compile(decoding_fn, mode="reduce-overhead", fullgraph=True)`. This will send the full [[CUDAGraph]] to the GPU with pre-compiled instructions.

#### 1.2. Increase the batch size

Increasing the batch size will move the problem to be closer to a CPU-bound problem rather than a memory-bound problem.

However, a batch size too big will result in the GPU being out of memory to calculate inference. Consider that the GPU needs space both for the KV-Cache and the model parameters. This note also applies to the sequence length to be inferred.
### 2. Setup a bigger cache for the pre-fill of the KV-Cache

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

### 3. Use vLLM or paged-attention

Both these techniques work as a middle-step between the memory available and the memory required. It's very similar to another level of memory where chunks of it are loaded in the device while the rest of it is paged and kept in a lower level.

### 4. Incorporate FlashAttention

Instead of storing the full attention matrix in the HBM, do block-wise computation of the dot product, such that all the computation is performed in the L2 cache.

### 5. Quantize the weights

Consider quantizing down the weights to `int8`. This, in part, reduces the space required to load the model in memory. It also might come with extra benefits on the speed of the operations.

Note that further quantizing does not equal better speed, there is a trade-off for each model, so find out which is your case.
### 6. Use speculative-decoding

Unfortunately, this requires a second model, but the good news is that it might not be terribly complex as it can be derived from the first model.

Alternatively, consider multi-query attention, which seems to be similar in principle. ( #TODO investigate further.)

### 5. [[GPTQ]]

Post-training (further) quantization

### 6. Apply tensor-paralellism

Running the code in multiple devices at the same time will accelerate the inference, at the expense of cost.

Some of results of these examples can be seen at https://github.com/pytorch-labs/gpt-fast

## Sources

- [Accelerating Generative AI with PyTorch II: GPT, Fast](https://pytorch.org/blog/accelerating-generative-ai-2/), PyTorch blog
- [Towards 100x Speedup: Full Stack Transformer Inference Optimization](https://yaofu.notion.site/Towards-100x-Speedup-Full-Stack-Transformer-Inference-Optimization-43124c3688e14cffaf2f1d6cbdf26c6c), Yao Fu
- [vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention](https://blog.vllm.ai/2023/06/20/vllm.html), vLLM Team
- Chen, Carol. "Transformer Inference Arithmetic", https://kipp.ly/blog/transformer-inference-arithmetic/, 2022.
