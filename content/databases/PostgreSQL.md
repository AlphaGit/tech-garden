---
title: PostgreSQL
tags:
- databases
- postgresql
- snippets
---

Client: `psql`

To login with a specific username: `psql -U <user>`


To login with username and password:

```bash
PGPASSWORD=<password> psql -U <user>
```

([Source](https://stackoverflow.com/a/6405296/147507))

Show tables: `\dt`, or `\dt+` to include sizing information.

