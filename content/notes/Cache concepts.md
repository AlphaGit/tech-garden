---
title: Cache concepts
tags:
- cache
---

## Sharding
Distributing the keys of the cache in multiple cache instances. There's usually a function that determines which key goes in which instance. (Hashing.)

## Consistent Hashing
A consistent hashing function can make it so that the keys are predictable distributed across multiple instances.

## Cache avalanche
Situation that happens when several keys in a single cache instance expire in a short period of time. This creates a lot of cache misses in a short period of time, creating extra burden on the original data storage.

It can be prevented with **staggered expiration**, where the inserted cache keys are given a TTL plus a random portion of time.

Consisent hashing and sharding helps prevent this problem.

## Cache stampede
Also called "thundering herd", it is similar to cache avalanche, but caused when there's a sudden usage of the system, causing extra load in the cache instances.

Consistent hashing and sharding helps prevent this problem.

## Cache penetration
Situation that happens when there are multiple requests trying to access non-existent data, that will result in cache misses and extra queries to the original data source.

Storing a representation of missing data in the cache helps prevent this problem.

## Hot key problem
Situation that happens when a particular key becomes more used than others, resulting in extra load on one specific cache instance.

An approach to solving this issue is duplicating the hot key across multiple nodes and accessing them through a round-robin scheme.

## Large key problem
Keys that have a value larger than most others will consume extra resources for storage and network, creating extra latency.

An approach to solving this issue is distributing the value of the key across multiple cache nodes. However, notice that this will create multiple round trips to get the full value. This distributes the network load across cache nodes but increases the amount of time to get that particular key.

## Cache persistence to disk
### Write-through strategy
Cache storage strategy where the value is stored in disk and then reported as stored by the cache.

### Write-back strategy
Cache storage strategy where the value is reported as stored by the cache and then stored in disk. This improves performance of storage at the risk of failure to store and subsequent cache misses.

