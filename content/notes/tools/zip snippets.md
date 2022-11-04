---
title: zip snippets
tags:
- zip
- command line
- unix
- snippets
---

Compressing a directory recursively but leaving some files/directories aside ([source](https://superuser.com/a/312302)):

```bash
zip -9r myarchive.zip . -x ignoreDir1\* ignoreFile1.xxx
```
