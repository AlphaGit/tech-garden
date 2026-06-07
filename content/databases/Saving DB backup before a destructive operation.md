---
title: Saving DB backup before a destructive operation
tags:
  - postgresql
  - databases
  - snippets
  - sql
---

Here's a quick and easy way to. store information in a backup table before making any destructive action:

```sql
create table test_bkp
as
select *
from test
where test."value" = 1

-- just confirming that data is there
select *
from test_bkp

delete
from test
where test."value" = 1
```
