---
title: BEIR
tags:
  - nlp
  - benchmark
  - ai
  - papers
---
Benchmark for Zero-shot evaluation of Information Retrieval Models

Paper: https://arxiv.org/abs/2104.08663
BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models

> Existing neural information retrieval (IR) models have often been studied in homogeneous and narrow settings, which has considerably limited insights into their out-of-distribution (OOD) generalization capabilities. To address this, and to facilitate researchers to broadly evaluate the effectiveness of their models, we introduce Benchmarking-IR (BEIR), a robust and heterogeneous evaluation benchmark for information retrieval[^BEIR]

> [BEIR](https://arxiv.org/abs/2104.08663?ref=txt.cohere.com) is a benchmark focused on out-of-domain information retrieval. Originally it consisted of 18 datasets, but now, just 14 are publically available (and due to license changes for the Twitter API, one dataset can no longer be accessed). We benchmarked all 18 datasets, but focused on the 14 publicly available datasets to allow easier reproduction.
> 
> The BEIR paper shows that out-of-domain information retrieval is especially challenging for text embedding models, which perform well on their trained datasets, but struggle when applied to other datasets and domains. As most users don't have training data for their data, out-of-domain performance is the most critical indicator for embedding models.[^Embedv3]

[^Embedv3]: [Embed v3](https://txt.cohere.com/introducing-embed-v3/)
[^BEIR]: [BEIR](https://arxiv.org/abs/2104.08663)