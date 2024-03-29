---
title: "Mamba: Linear-Time Sequence Modeling with Selective State Spaces"
tags:
  - ai
  - nlp
  - llm
  - performance
  - papers
  - to_complete
---
https://arxiv.org/pdf/2312.00752.pdf

> Many subquadratic-time architectures such as linear attention, gated convolution and recurrent models, and [[Structured State Space Models |structured state space models (SSMs)]] have been developed to address [[Transformers]]’ computational inefficiency on long sequences, but they have not performed as well as attention on important modalities such as language.
> We identify that a key weakness of such models is their inability to perform content-based reasoning, and make several improvements. First, simply letting the SSM parameters be functions of the input addresses their weakness with discrete modalities, allowing the model to selectively propagate or forget information along the sequence length dimension depending on the current token. Second, even though this change prevents the use of efficient convolutions, we design a hardware-aware parallel algorithm in recurrent mode. We integrate these selective SSMs into a simplified end-to-end neural network architecture without attention or even MLP blocks (Mamba).
> Mamba enjoys fast inference (5× higher throughput than Transformers) and linear scaling in sequence length, and its performance improves on real data up to million-length sequences.