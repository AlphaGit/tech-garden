---
title: Bloom filter
tags:
  - data_structures
  - algorithms
  - cache
---
Bloom filters are probabilistic data structures: they can test for the non-membership of an element with 100% certainty, but they can't give 100% certainty about the membership of an element.

```typescript
let bf = new BloomFilter();
bf.add("Ant");
bf.add("Rhino");
bf.contains("Bear"); // false → we know 100% is not a member
bf.contains("Rhino"); // true → might or might not be a member
```

Bloom filters are popular because of their savings in space.

Internally, they're an array of bits, which are set by the members being passed through $N$ hash functions. When a membership is checked, if those exact bits are not set, we know for a fact that the element was not present, but if all the bits are set, they might be a result of collisions, meaning we can't know for sure.

Note that because of this design, **elements cannot be removed from a bloom filter**.

## Counting bloom filters

A variation is to store numbers in each positions instead of a bit that's only set/not set. This allows for elements to be "removed" so that the other elements are not removed accidentally. However, removing elements that had not been entered in the first place (which we can't test for with 100% certainty) is a possibility, meaning that we introduce the chance for false-negatives too.

## Choosing parameters

Optimal number of hash functions, which minimizes the error rate:

$$k = \frac{m}{n} \ln 2$$
Where $k$ is the number of hash functions, $m$ is the number of bits that the bloom filter is composed of, $n$ is the number of elements to be stored.

However, if we know of an acceptable error rate ($\varepsilon$), this means we can calculate the amount of bits:

$$m = -\frac{n \ln(\varepsilon)}{\ln(2)^2}$$

## Sources

- [Bloom Filters - Sam Who](https://samwho.dev/bloom-filters/)
- [Bloom filter - Wikipedia](https://en.wikipedia.org/wiki/Bloom_filter)