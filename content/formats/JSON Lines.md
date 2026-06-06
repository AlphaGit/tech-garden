---
title: JSON Lines
tags:
  - formats
  - json
  - to_complete
---

> JSON Lines is a convenient format for storing structured data that may be processed one record at a time.

## Requirements

> 1. UTF-8 Encoding
> 2. Each Line is a Valid JSON Value
> 3. Line Separator is `'\n'`

## Suggestions

> - JSON Lines files may be saved with the file extension `.jsonl`.
> - Stream compressors like `gzip` or `bzip2` are recommended for saving space, resulting in `.jsonl.gz` or `.jsonl.bz2` files.
> - MIME type may be `application/jsonl`

## Sources

- [JSON Lines website](https://jsonlines.org/)
- [GitHub repository](https://github.com/wardi/jsonlines)