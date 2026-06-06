---
title: API Gateway
tags:
  - architecture
---
An API gateway acts as a single entry point for client requests. The API gateway is responsible for request routing, composition, and protocol translation. It also provides additional features like authentication, authorization, caching, and rate limiting.

The API Gateway:

- parses and validates the attributes in the HTTP request.
- checks allow/deny lists.
- authenticates and authorizes through an identity provider.
- applies rate-limiting rules.
- routes the request to the relevant backend service by path matching.
- transforms the request into the appropriate protocol and forwards it to backend microservices.
- handles any errors that may arise during request processing for graceful degradation of service.
- implements resiliency patterns like [[circuit brakes]] to detect failures and prevent overloading interconnected services, avoiding cascading failures.
- utilizes observability tools for logging, monitoring, tracing, and debugging.
- can optionally cache responses to common requests to improve responsiveness.

The API gateway is different from a load balancer. While both handle network traffic, the API gateway operates at the application layer, mainly handling HTTP requests; the load balancer mostly operates at the transport layer.[^bbg]

[^bbg]: [ByteByteGo: 6 More Microservices Interview Questions](https://blog.bytebytego.com/p/6-more-microservices-interview-questions)