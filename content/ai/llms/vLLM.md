---
title: vLLM
tags:
  - ai
  - llm
---
 vLLM utilizes **PagedAttention**, our new attention algorithm that effectively manages attention keys and values. vLLM equipped with PagedAttention redefines the new state of the art in LLM serving: it delivers up to 24x higher throughput than HuggingFace Transformers, without requiring any model architecture changes.

 In the autoregressive decoding process, all the input tokens to the LLM produce their attention key and value tensors, and these tensors are kept in GPU memory to generate next tokens. These cached key and value tensors are often referred to as KV cache. The KV cache is

- _Large:_ Takes up to 1.7GB for a single sequence in LLaMA-13B.
- _Dynamic:_ Its size depends on the sequence length, which is highly variable and unpredictable.

PagedAttention partitions the KV cache of each sequence into blocks, each block containing the keys and values for a fixed number of tokens. During the attention computation, the PagedAttention kernel identifies and fetches these blocks efficiently.

PagedAttention has another key advantage: efficient memory sharing. For example, in _parallel sampling_, multiple output sequences are generated from the same prompt.

PageAttention’s memory sharing greatly reduces the memory overhead of complex sampling algorithms, such as parallel sampling and beam search, cutting their memory usage by up to 55%.

## Sources

- [vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention](https://blog.vllm.ai/2023/06/20/vllm.html)

