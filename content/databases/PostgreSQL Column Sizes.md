---
title: PostgreSQL Column Sizes
tags:
  - postgresql
  - databases
  - snippets
  - sql
---
Here's a handy script to calculate row and actual column sizes[^1][^2]:

```sql
create or replace function column_sizes(target_table regclass) 
    returns table (column_name text, column_size bigint) 
    language plpgsql stable parallel restricted as $function$
declare 
    rec record;
    parsed_target_table text[]:=parse_ident(target_table::text);
    schema_name text:=case when parsed_target_table[2] is not null then
      parsed_target_table[1] end;
    table_name text:=parsed_target_table[array_upper(parsed_target_table,1)];
begin
    for rec in execute format(' select  column_name 
                                from    information_schema.columns 
                                where   (%1$L is null or table_schema = %1$L) 
                                and     (%2$L is null or table_name   = %2$L)',
                                schema_name,
                                table_name  ) loop
        return query execute format(
            'select %1$L,sum(pg_column_size(%1$I))::bigint from %s',
             rec.column_name,
             target_table);
    end loop;
end $function$;
```

Usage:

```sql
select * from column_sizes('schema.table');
```

However, this function can be really intensive for tables with lots of rows since it will have to process each of them. If rows are fairly consistent and any of them can be representative of the whole set, consider using only the first one:

```sql
create or replace function column_sizes(target_table regclass) 
    returns table (column_name text, column_size bigint) 
    language plpgsql stable parallel restricted as $function$
declare 
    rec record;
    parsed_target_table text[]:=parse_ident(target_table::text);
    schema_name text:=case when parsed_target_table[2] is not null then
      parsed_target_table[1] end;
    table_name text:=parsed_target_table[array_upper(parsed_target_table,1)];
begin
    for rec in execute format(' select  column_name 
                                from    information_schema.columns 
                                where   (%1$L is null or table_schema = %1$L) 
                                and     (%2$L is null or table_name   = %2$L)',
                                schema_name,
                                table_name  ) loop
        return query execute format(
            'select %1$L pg_column_size(%1$I)::bigint from %s limit 1',
             rec.column_name,
             target_table);
    end loop;
end $function$;
```

Alternatively, consider using a subset of rows, which could be done by obtaining a random subset and summing them, then diving it by the amount of rows (not shown here).

[^1]: [Size of every column Postgres (StackOverflow)](https://stackoverflow.com/questions/75729709/size-of-every-column-postgres)
[^2]: [Size of every column Postgres (StackOverflow) (demo)](https://dbfiddle.uk/wtnwh8v7)