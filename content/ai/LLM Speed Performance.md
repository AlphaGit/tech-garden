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
There are different techniques that can be done on an LLM to improve their speed.

From [Accelerating Generative AI with PyTorch II: GPT, Fast](https://pytorch.org/blog/accelerating-generative-ai-2/), the following techniques are present:

1. Reduce the roundtrips between CPU-GPU/

Use `torch.compile(decoding_fn, mode="reduce-overhead", fullgraph=True)`. This will send the full [[CUDAGraph]] to the GPU with pre-compiled instructions.

2. Setup a bigger cache for the pre-fill of the KV-Cache

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

3. Quantize the weights. Note that further quantizing does not equal better speed, there is a trade-off for each model, so find out which is your case.

4. Use speculative-decoding. Unfortunately, this requires a second model, but the good news is that it might not be terribly complex as it can be derived from the first model.

5. [[GPTQ]]: Post-training (further) quantization

6. Apply tensor-paralellism

The results of these examples can be seen at https://github.com/pytorch-labs/gpt-fast