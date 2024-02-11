---
title: Redis AOF (Append Only File)
tags:
  - redis
  - databases
---
AOF persistence logs every write operation received by the server. These operations can then be replayed again at server startup, reconstructing the original dataset. Commands are logged using the same format as the Redis protocol itself.[^redis]

Unlike a write-ahead log, the Redis AOF log is a write-after log. Redis executes commands to modify the data in memory first and then writes it to the log file.[^bbg91]

[^bbg91]: [ByteByteGo EP91: REST API Authentication Methods](https://blog.bytebytego.com/p/ep91-rest-api-authentication-methods)
[^redis]: [Redis persistence](https://redis.io/docs/management/persistence/)