---
title: Glitch tokens
tags:
- ai
- tokenization
- llms
- ml
---

> A fascinating subset of tokens are what are known as “glitch tokens”.
> 
> \[...]
> 
> > These glitch tokens are all near the centroid of the token embedding space. That means that the model cannot really differentiate between these tokens and the others equally near the center of the embedding space, and therefore when asked to ’repeat’ them, gets the wrong one.
> 
> [^1]

> - Many of these tokens reliably break determinism in the OpenAI GPT-3 playground at temperature 0 (which theoretically shouldn't happen).
> - 
> \[...]
> 
> The anomalous tokens may be those which had very little involvement in training, so that the model “doesn’t know what to do” when it encounters them, leading to evasive and erratic behaviour. This may also account for their tendency to cluster near the centroid in embedding space, although we don't have a good argument for why this would be the case.
> 
> The non-determinism at temperature zero, we guess, is caused by floating point errors during forward propagation. Possibly the “not knowing what to do” leads to maximum uncertainty, so that logits for multiple completions are maximally close and hence these errors (which, despite a lack of documentation, GPT insiders inform us are a known, but rare, phenomenon) are more reliably produced.
> 
> [^2]

[^1]: [Understanding GPT Tokenizers](https://simonwillison.net/2023/Jun/8/gpt-tokenizers/), Simon Willison’s Weblog
[^2]: [SolidGoldMagikarp (plus, prompt generation)](https://www.lesswrong.com/posts/aPeJE8bSo6rAFoLqg/solidgoldmagikarp-plus-prompt-generation), by Jessica Rumbelow, mwatkins @ LessWrong
