---
title: Docker snippets
tags:
- tools
- docker
- command line
- containers
---

Useful docker snippets for the delight of every day use.

Getting the IP address of a running docker container ([source](https://stackoverflow.com/a/20686101/147507)):

```bash
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id
```
