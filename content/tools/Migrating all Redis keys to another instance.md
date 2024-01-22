---
title: Migrating all Redis keys to another instance
tags:
  - snippets
  - redis
  - bash
  - command_line
---
```bash
redis-cli --scan --pattern "*" | xargs -I{} redis-cli migrate <destIP> <destPort> 0 5000 COPY REPLACE KEYS {}
```
