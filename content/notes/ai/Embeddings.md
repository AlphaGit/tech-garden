---
title: Embeddings
tags:
  - ai
  - theory
  - papers
  - model
---
Embeddings turn a piece of content into an array of floating point numbers.

> The key thing about that array is that it will always be the same length, no matter how long the content is. The length is defined by the embedding model you are using.
>
> Imagine it as co-ordinates in a very weird multi-dimensional space.
>
> The location within the space represents the semantic meaning of the content, according to the embedding model’s weird, mostly incomprehensible understanding of the world.[^EmbeddingsWilson]

Example of usage:

> I currently have 472 articles on my site. I calculated the 1,536 dimensional embedding vector (array of floating point numbers) for each of those articles, and stored those vectors in my site’s [[SQLite]] database.
>
> Now, if I want to find related articles for a given article, I can calculate the _[[cosine similarity]]_ between the embedding vector for that article and every other article in the database, then return the 10 closest matches by distance.
>
> Here’s [the Python function](https://github.com/simonw/llm/blob/bf229945fe57036fa75e8105e59d9e506a720156/llm/__init__.py#L252C1-L256C53) I’m using to calculate those [[cosine similarity]] distances:

```python
def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))
    magnitude_a = sum(x * x for x in a) ** 0.5
    magnitude_b = sum(x * x for x in b) ** 0.5
    return dot_product / (magnitude_a * magnitude_b)
```
[^EmbeddingsWilson]

Another kind of embedding models are [[Word2Vec]], [[CLIP]].
## Average Locations

> Another trick with embeddings is to use them for classification.
> 
> First calculate the average location for a group of embeddings that you have classified in a certain way, then compare embeddings of new content to those locations to assign it to a category.
> 
> Amelia Wattenberger demonstrated a beautiful example of this in [Getting creative with embeddings](https://wattenberger.com/thoughts/yay-embeddings-math).[^EmbeddingsWilson]

Another interesting usage of embedding models is powering [[Retrieval Augmented Generation]].

## Embeddings
- [[Word2Vec]]
- [[GloVe]]
- [[Embed v3]]

[^EmbeddingsWilson]: [Embeddings: what they are and why they matter](https://simonwillison.net/2023/Oct/23/embeddings/), Simon Willson