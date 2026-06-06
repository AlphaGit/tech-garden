---
title: curl
tags:
  - tools
  - unix
  - command_line
---

**curl** is an amazing tool to perform HTTP calls.

Some less known features of it are:

## URL templates
**curl** accepts a certain level of "templating" in its URLs:

```bash
curl https://www.google.com/search?q={a,b}&t=[1-10]
```

Will generate the following (sequential) HTTP calls:

```text
https://www.google.com/search?q=a&t=1
https://www.google.com/search?q=a&t=2
https://www.google.com/search?q=a&t=3
https://www.google.com/search?q=a&t=4
https://www.google.com/search?q=a&t=5
https://www.google.com/search?q=a&t=6
https://www.google.com/search?q=a&t=7
https://www.google.com/search?q=a&t=8
https://www.google.com/search?q=a&t=9
https://www.google.com/search?q=a&t=10
https://www.google.com/search?q=b&t=1
https://www.google.com/search?q=b&t=2
https://www.google.com/search?q=b&t=3
https://www.google.com/search?q=b&t=4
https://www.google.com/search?q=b&t=5
https://www.google.com/search?q=b&t=6
https://www.google.com/search?q=b&t=7
https://www.google.com/search?q=b&t=8
https://www.google.com/search?q=b&t=9
https://www.google.com/search?q=b&t=10
```

However, these will be sequential and executed one at a time. If we wanted to parallelize them, we can make use of the `-P` parameter (that will allow multiple connections), but `curl` needs to be called through [[xargs]].

## Different options for multiple calls
curl accepts multiple URLs to perform requests:

```bash
curl https://www.google.com/search?q=a https://www.google.com/search?q=b
```

However, the same options will apply for each of them. If we wanted to change them, we can use the `-:` or `--next` option:

```bash
curl https://www.google.com/search?q=a -: -X 'POST' https://www.google.com/search?q=b
```

## Sources
- [How can I run multiple curl requests processed sequentially?](https://stackoverflow.com/q/3110444/147507)
- [Download a sequence of files with curl](https://electrictoolbox.com/curl-download-sequence-files/)
- [How to quickly stress test a web server](https://tweenpath.net/how-to-quickly-stress-test-a-web-server/)