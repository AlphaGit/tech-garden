---
title: MTEB (Massive Text Embedding Benchmark)
tags:
  - ai
  - benchmark
  - research
  - ml
  - nlp
  - embedding
  - papers
---
> MTEB consists of 58 datasets covering 112 languages from 8 embedding tasks: Bitext mining, classification, [[clustering]], pair classification, reranking, retrieval, STS and summarization.

## Tasks

> **Bitext Mining:** Inputs are two sets of sentences from two different languages. For each sentence in the first set, the best match in the second set needs to be found.
> 
> **Classification:** A train and test set are embedded with the provided model. The train set embeddings are used to train a logistic regression classifier with 100 maximum iterations, which is scored on the test set.
> 
> **Clustering:** Given a set of sentences or paragraphs, the goal is to group them into meaningful clusters.
> 
> **Pair Classification:** A pair of text inputs is provided and a label needs to be assigned. Labels are typically binary variables denoting duplicate or paraphrase pairs. 
> 
> **Reranking:** Inputs are a query and a list of relevant and irrelevant reference texts. The aim is to rank the results according to their relevance to the query.
> 
> **Retrieval:** Each dataset consists of a corpus, queries and a mapping for each query to relevant documents from the corpus. The aim is to find these relevant documents.1
> 
> **Semantic Textual Similarity (STS):** Given a sentence pair the aim is to determine their similarity. Labels are continuous scores with higher numbers indicating more similar sentences.
> 
> **Summarization:** A set of human-written and machine-generated summaries are provided. The aim is to score the machine summaries.
---

Code available at: https://github.com/embeddings-benchmark/mteb

Leaderboard in HuggingFace: https://huggingface.co/spaces/mteb/leaderboard

[^MTEB]: [MTEB: Massive Text Embedding Benchmark](https://arxiv.org/pdf/2210.07316.pdf)
