---
title: EVA-Bench
tags:
  - ai
  - benchmark
  - nlp
  - ml
  - papers
  - dataset
  - voice
  - agents
---

End-to-end benchmark for evaluating **voice agents** in realistic enterprise settings, built by ServiceNow-AI.

Website: https://servicenow.github.io/eva
Paper: https://arxiv.org/abs/2605.13841
Code: https://github.com/ServiceNow/eva
Dataset: https://huggingface.co/datasets/ServiceNow-AI/eva-bench
Leaderboard: https://servicenow.github.io/eva/#results

> Voice agent failures are often highly domain-specific. A system that flawlessly processes alphanumeric confirmation codes in flight re-booking transactions might stumble when handling complex policies in HR systems. EVA-Bench expands from one enterprise domain to three: Airline Customer Service Management (CSM), Enterprise IT Service Management (ITSM), and Healthcare HR Service Delivery (HRSD). Together they span **213 evaluation scenarios across 121 tools**, a roughly 4x increase in scenario coverage from the original release.[^EvaData]

Every scenario was validated for solvability against three frontier models (OpenAI GPT-5.4, Google Gemini 3.1 Pro, and Anthropic Claude Opus 4.6), so the benchmark is meant to be both challenging and fair. It is open-source under the MIT license.

## Domains

| Config    | Domain                                    | Scenarios |
| --------- | ----------------------------------------- | --------- |
| `airline` | Airline Customer Service Management (CSM) | 50        |
| `itsm`    | Enterprise IT Service Management (ITSM)   | 80        |
| `medical` | Healthcare HR Service Delivery (HRSD)     | 83        |

All three require accurate transcription of structured named entities over voice (e.g. confirmation codes and employee identifiers) but differ in their primary challenge and number of tools.

## Where it can be used

EVA-Bench is built for two audiences:

- **Evaluating a voice agent** — run an agent against a diverse set of realistic enterprise scenarios spanning 35+ distinct workflows, including authentication flows (a consistent failure point for voice agents), multi-intent calls, and adversarial callers who try to bypass troubleshooting, misclassify urgency, or access records they are not authorized to view.
- **Building your own evaluation dataset** — the generation and validation process (joint generation of user goal + initial DB + ground-truth final DB via the graph-based [SyGra](https://github.com/ServiceNow/SyGra) pipeline, plus a multi-stage validation loop) is documented in enough detail to serve as a practical reference.

Each record contains a structured user goal, an initial scenario database, and a ground-truth expected final database state — everything needed to run a full bot-to-bot evaluation. A multilingual extension (e.g. French, with localized names, locations, emails, and phone numbers) is in progress.

## Minimal examples

Load any of the three configs with the Hugging Face `datasets` library:

```python
from datasets import load_dataset

# Airline Customer Service Management (CSM) — 50 scenarios
airline = load_dataset("ServiceNow-AI/eva-bench", "airline", split="test")

# Enterprise IT Service Management (ITSM) — 80 scenarios
itsm = load_dataset("ServiceNow-AI/eva-bench", "itsm", split="test")

# Healthcare HR Service Delivery (HRSD) — 83 scenarios
hrsd = load_dataset("ServiceNow-AI/eva-bench", "medical", split="test")
```

Inspect a single scenario's three jointly-consistent components:

```python
record = airline[0]
record["user_goal"]          # decision-tree-structured caller intent + negotiation sequence
record["initial_database"]   # backend state the agent's tools query/modify
record["expected_database"]  # ground-truth final state verifiers check against
```

For the full evaluation harness, setup instructions, and contributing guidelines, see the [GitHub repo](https://github.com/ServiceNow/eva).

## Related

- [[NLP Benchmarks]] — benchmark index
- [[LLM Benchmarks]]
- [[HotpotQA]], [[BEIR]], [[MTEB]]

[^EvaData]: [EVA-Bench Data 2.0: 3 Domains, 121 Tools, 213 Scenarios](https://huggingface.co/blog/ServiceNow-AI/eva-bench-data) (ServiceNow-AI, June 4, 2026)

[^EvaPaper]: [EVA-Bench: A New End-to-end Framework for Evaluating Voice Agents](https://arxiv.org/abs/2605.13841) (Bogavelli et al., 2026)
