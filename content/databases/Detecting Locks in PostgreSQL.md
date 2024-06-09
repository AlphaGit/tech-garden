---
title: Detecting Locks in PostgreSQL
tags:
  - postgresql
  - databases
  - snippets
  - sql
---
This snippet shows the locks currently present in the database for a specific table of a specific namespace. By changing the filters you can see all the locks that are not restricted to tables.

```sql
SELECT
    l.locktype,
    l.mode,
    l.granted,
    c.relname ,
    a.usename AS locked_by,
    a.query AS blocking_query,
    a.pid,
    n.nspname AS schema_name
FROM pg_locks l
JOIN pg_stat_activity a ON l.pid = a.pid
JOIN pg_class c ON l.relation = c.oid
JOIN pg_namespace n ON c.relnamespace = n.oid
WHERE n.nspname = '<your namespace>'
    AND c.relname = '<your table>'
ORDER BY l.granted DESC;
```

Also, the `pid` value shows the process connection associated to it, which can be killed in the following way to release the lock:

```sql
SELECT pg_terminate_backend(<pid>)
```