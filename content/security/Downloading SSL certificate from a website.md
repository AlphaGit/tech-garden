---
tags:
- snippets
- ssl
- bash
title: Downloading SSL certificate from a website
---

[Source](https://serverfault.com/a/192731/90562)

```bash
echo -n
  | openssl s_client -connect $HOST:$PORTNUMBER -servername $SERVERNAME \
  | openssl x509 > /tmp/$SERVERNAME.cert
```