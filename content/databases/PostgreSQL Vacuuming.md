---
title: PostgreSQL Vacuuming
tags:
  - postgresql
  - databases
  - maintenance
  - snippets
  - sql
---

## Vacuuming

The vacuuming process in PostgreSQL is an essential maintenance operation that helps optimize database performance and manage storage. Here are the key aspects of PostgreSQL's vacuuming process:

1. Purpose:
   - Reclaims storage occupied by dead tuples (rows that have been deleted or updated)[^1][^2]
   - Prevents transaction ID wraparound issues[^2]
   - Updates statistics for the query planner[^2]
   - Improves overall query performance[^3]

2. Types of VACUUM:
   - Standard VACUUM: Reclaims space and makes it available for reuse within the same table[^1]
   - VACUUM FULL: Rewrites the entire table, reclaiming more space but requiring an exclusive lock and more time[1][3]

3. Autovacuum:
   - PostgreSQL includes an autovacuum daemon that automatically performs VACUUM operations[^2]
   - It schedules vacuuming dynamically based on update activity[^2]

4. How it works:
   - Scans tables to remove dead tuples resulting from UPDATE and DELETE operations[^3]
   - Marks space occupied by dead tuples as reusable by other tuples[^3]
   - Updates system catalogs with current statistics[^3]

5. Concurrent operation:
   - Standard VACUUM can run in parallel with normal database operations (SELECT, INSERT, UPDATE, DELETE)[^1]
   - VACUUM FULL requires an ACCESS EXCLUSIVE lock and cannot run concurrently with other table operations[^1]

6. Performance considerations:
   - VACUUM creates I/O traffic, which can impact performance of other active sessions[^2]
   - Configuration parameters can be adjusted to reduce the performance impact of background vacuuming[^2]

7. Frequency:
   - Regular vacuuming is necessary, especially for frequently updated tables[^1]
   - The frequency depends on the database's update rate and available resources[^2]

8. Best practices:
   - Use autovacuum for most situations, adjusting its parameters as needed[^2]
   - Schedule manual VACUUMs during low-usage periods if necessary[^2]
   - Use VACUUM FULL sparingly, only when significant space needs to be reclaimed[^2]

9. Monitoring:
   - It's important to monitor VACUUM processes to ensure they're running efficiently[^4]
   - You can query `pg_stat_user_tables` to check when tables were last vacuumed[^4]

By regularly performing VACUUM operations, either through autovacuum or manual scheduling, PostgreSQL can maintain optimal performance, manage disk space effectively, and prevent potential issues related to transaction ID wraparound.

## Vacuuming progress

Aside from executing a `VACUUM VERBOSE`, vacuuming process, which will output the different steps it is executing, this approach can approximate the level of progress of the vacuuming process.[^6]

```sql
SELECT
	heap_blks_scanned/CAST(heap_blks_total AS NUMERIC) * 100 AS heap_blks_percent,
	progress.*,
	activity.query
FROM pg_stat_progress_vacuum AS progress
INNER JOIN pg_stat_activity AS activity ON activity.pid = progress.pid;
```

[^1]: https://www.postgresql.org/docs/current/sql-vacuum.html

[^2]: https://www.postgresql.org/docs/current/routine-vacuuming.html

[^3]: https://www.enterprisedb.com/blog/postgresql-vacuum-and-analyze-best-practice-tips

[^4]: https://www.datadoghq.com/blog/postgresql-vacuum-monitoring/

[^5]: https://www.enterprisedb.com/postgres-tutorials/how-does-vacuum-work-postgresql

[^6]: https://dba.stackexchange.com/a/245163/2704
