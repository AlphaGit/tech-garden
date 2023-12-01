---
title: Semantic Search
tags:
  - ai
  - nlp
  - search
---
>_Semantic Search_ is a search method for surfacing highly relevant results based on the **meaning** of the query, context, and content. It goes beyond simple keyword indexing or filtering. It allows users to find things more naturally and with better support for nuance than highly sophisticated but rigid traditional relevancy methods. In practice, it feels like the difference between asking a real person or talking to a machine.

> Many solutions today rely on _[[ai/Embeddings|document embeddings]]_ - representing meaning as vectors. Since semantic search alone may not provide sufficient relevant hits, traditional full-text search is often used to supplement results. A feedback loop based on user interactions (clickes, likes, etc.) provides input to continuously improve relevancy.

> The key processes are: **indexing**, **querying**, and **tracking**

> **Indexing** is done by converting a document’s content to an embeddings vector through a text-to-vector encoder.

![[BBG Semantic Search worklow.png]]

> **Querying** relies on encoding incoming queries into vectors, preferably using the same encoder as indexing. These vectors are used to query the vector database. These results are combined with traditional full-text search results and re-ranked for improved relevancy. This combination of semantic and full-text search is referred to as “hybrid search”.

> **Tracking** involves capturing important user interactions - e.g. clicking on results, liking items, etc. These events are used to update the machine learning models that power re-ranking. This creates a feedback loop, leveraging user behaviors to continuously improve search relevancy.[^BBG]

[^BBG]: [Unlock Highly Relevant Search with AI](https://blog.bytebytego.com/p/unlock-highly-relevant-search-with), ByteByteGo