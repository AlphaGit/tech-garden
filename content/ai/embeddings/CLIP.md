---
title: CLIP
tags:
  - ai
  - model
  - embedding
---
> My current favorite embedding model is [CLIP](https://openai.com/blog/clip/).
> 
> [[CLIP]] is a fascinating model released by [[OpenAI]]—back in January 2021, when they were still doing most things in the open—that can embed both text and images.
> 
> Crucially, it embeds them both into the same vector space.
> 
> If you embed the string “dog”, you’ll get a location in 512 dimensional space (depending on your CLIP configuration).
> 
> If you embed a photograph of a dog, you’ll get a location in that same space... and it will be close in terms of distance to the location of the string “dog”!
> 
> This means we can search for related images using text, and search for related text using images.
> 
> I built [an interactive demo](https://observablehq.com/@simonw/openai-clip-in-a-browser) to help explain how this works. The demo is an [[Observable notebook]] that runs the [[CLIP]] model directly in the browser.[^EmbeddingsWilson]

[^EmbeddingsWilson]: [Embeddings: what they are and why they matter](https://simonwillison.net/2023/Oct/23/embeddings/), Simon Willson