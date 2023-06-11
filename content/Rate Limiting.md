---
title: Rate Limiting
tags:
- rate limiting
- architecture
---

## Concepts

**Fail Open**: strategy for rate limiters to let all transactions go through when they are not available. It has the benefit of not stopping legitimate requests, but they could overwhelm the underlying system if they suffer an amount of requests bigger than they can handle.

**Fail Close:** strategy for rate limiters to close up and reject all transactions when they are not available. It protects the system from possible overload, but it will generate downtime for consumers.

**Token Bucket Algorithm:** Approach to rate limiting. With a certain frequency, a certain amount of tokens are "added" into a bucket, up to a maximum of the bucket capacity. Each request has a cost of a certain amount of tokens. If the bucket contains said amount or more, the request is allowed, otherwise it is rejected.

## Other considerations

Rate limiters will always be part of the critical path of execution for requests. As such, consider a kill switch or a feature flag to disable them completely if they were to misbehave.

Rate limiters should always provide clear rejection messages, so that clients know that their request needs not to be retried. Usually HTTP Status 429 (Too Many Requests) or HTTP Status 503 (Service Unavailable). Consider including the [Retry-After](https://www.rfc-editor.org/rfc/rfc7231#section-7.1.3) HTTP header.

Consider dark-launching rate limiters before activating them. They should just log which requests would be rejected and from that analysis, you can understand if they're going to work correctly.

## Sources
- [Rate Limiter for the Real World](https://blog.bytebytego.com/p/rate-limiter-for-the-real-world), ByteByteGo Newsletter
