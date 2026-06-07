---
title: Model Unlearning
date created: 2025-10-20T15:48:28-04:00
date modified: 2025-10-20T16:22:09-04:00
---

_Unlearning_ is the re-training of a model to remove some knowledge so that it is not capable of responding to it.

It might be motivated by:

- legal necessity (e.g. right to be forgotten)
- alignment (e.g. prevent dangerous knowledge from being spread)
- general training (e.g. preventing very common data from being memorized)

[[LLM Benchmarks|Benchmarks]] for unlearning:

- WMDP[^1].
- TOFU[^8]

## Techniques for unlearning

### SISA[^3]

**S**harded, **I**solated, **S**liced, and **A**ggregated Training: Trains the original model in smaller composable models through [[Model Ensemble|ensembling]]. The data is partitioned across these individual models.
![[SISA Unlearning.png]]

## Differential Privacy[^4]

Applies noise and clips L2 Norm of per-example gradients for specific parts of the data that wants to be unlearned. The great benefit of this is that it provides a quantifiable demonstration of the unlearning happening, and reduces the impact of the model, as long as the differential (called $(\alpha, \beta)-\text{unlearning}$) are kept low enough to show that impact. This demonstrates the distributional closeness between the original model and the unlearned model, which would be (ideally) equivalent.

Liu's article[^2] covers the details of several approaches under differential privacy used for the [[#Unlearning Challenge]].

### Just ask

Some approaches just ask the model to pretend not to know about a subject with good results.[^6] this can even take the shape of in-context unlearning[^7], so that the model negates the weights of the provided examples. However, this does not impact the model and is not feasible for large datasets where lots of examples need to be unlearned.

## Unlearning Challenge

In 2023, NeurIPS hosted a Machine Unlearning Challenge[^5]

[^1]: [**W**eapons of **M**ass **D**estruction **P**roxy (WMDP) benchmark](https://www.wmdp.ai/), Li et al

[^2]: Liu, Ken Ziyu. (May 2024). Machine Unlearning in 2024. Stanford Computer Science. [https://ai.stanford.edu/~kzliu/blog/unlearning](https://ai.stanford.edu/~kzliu/blog/unlearning).

[^3]: [Machine Unlearning](https://arxiv.org/pdf/1912.03817). Bourtoule et al.

[^4]: [Deep Learning with Differential Privacy](https://arxiv.org/abs/1607.00133). Abadi et al.

[^5]: [NeurIPS 2023 Machine Unlearning Challenge](https://unlearning-challenge.github.io/)

[^6]: [Guardrail Baselines for Unlearning in LLMs](https://arxiv.org/abs/2403.03329), Thaker et al

[^7]: [In-Context Unlearning: Language Models as Few Shot Unlearners](https://arxiv.org/abs/2310.07579), Pawelczyk, Neel, Lakkaraju

[^8]: [TOFU: A Task of Fictitious Unlearning for LLMs](https://locuslab.github.io/tofu/), Maini et al
