---
title: Best input data format for LLMs
date created: 2025-10-06T21:54:21-04:00
date modified: 2025-10-06T21:55:47-04:00
tags:
  - ai
  - llm
  - formats
---

https://www.improvingagents.com/blog/best-input-data-format-for-llms

Test performed in September 2025 showing that the best format for LLMs to understand data is Markdown-KV:

````markdown
# Employee Database

## Record 1

```
id: 1
name: Charlie A0
age: 56
city: New York
department: Operations
salary: 67896
years_experience: 7
project_count: 1
```

## Record 2

```
id: 2
name: Grace B1
age: 59
city: Mumbai
department: Marketing
salary: 47248
years_experience: 0
project_count: 43
```

## Record 3

```
id: 3
name: Eve C2
age: 50
city: Singapore
department: Sales
salary: 102915
years_experience: 14
project_count: 11
```
````
