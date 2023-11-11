---
title: Command line snippets
tags:
- command line
- snippets
- bash
- zsh
---

## Delete files smaller than a certain size

([Source](https://superuser.com/a/644274))

```bash
find . -name "*.ext" -type f -size -160k -delete
```

For files bigger, use `-size +160k`.
For measuring in bytes directly use `-size -160c` .