---
title: Kubectl snippets
tags:
- kubernetes
- command line
- snippets
---

For the alias, see my [[dotfiles]] project.

Forward a port from a pod to access it from localhost:

```bash
kdev port-forward <pod-name> <local-port>:<pod-port>
```
