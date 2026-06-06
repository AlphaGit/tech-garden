---
title: Designing REST APIs Guidelines
tags:
  - http
  - api
  - design
  - architecture
  - guidelines
---
## 1. DO Use plural nouns for collections

```
# GOOD

GET /products
GET /products/{product_id}

# BAD
GET /product/{product_id}
```

## 2. DON'T add unnecessary path segments

```
# GOOD
GET /shop/{shop_id}
GET /listings/{listing_id}

# BAD
GET /shop/{shop_id}/listings/{listing_id}
```

(Assuming `listing_id` is globally unique and does not really require `shop_id`)

Aside from the problems for consumers[^JeffSnitzer], it always brings up the question of what to do if the child ID exists but the parent ID does not. The obvious answer is to reject the request, which leads you to doing a bunch of extra database calls for something you shouldn't need to in the first place.

## 3. DON'T add extensions to the URL

```
# GOOD
GET /products/{product_id}

# BAD
GET /products/{product_id}.json
```

Use HTTP headers instead.

## 4. DON'T return arrays as top level elements

```
# GOOD
GET /products
{"data": [{...product1...}, {...product2...}]}

# BAD
GET /products
[{...product1...}, {...product2...}]
```

Aside from the array constructor vulnerabilities[^JsonVuln], this design is not backwards compatible for further modifications[^JeffSnitzer].

## 5. DON'T return map structures

```
# GOOD
GET /products
{"data": [{...product1...}, {...product2...}]}

# BAD
GET /products
{
	"key1": {...product1...},
	"key2": { ...product2...}
}
```

## 6. DO use strings for identifiers

```
# GOOD
{ "id": "123" }

# BAD
{ "id": 123 }
```

Future integrations will thank you.

## 7. DO prefix your identifiers

```
# GOOD
{ "id": "prod_123" }
{ "id": "user_123" }

# BAD
{ "id": "123" }
```

You don't even need to store the prefixes.

## 9. DO use a structured error format

```
# GOOD
{
	"error": {
		"message": "Something went wrong",
		"code": 123,
		...
	}
}
```

Jeff Snitzer suggest including a `cause` recursive field that allows you to provide nested errors for easier troubleshooting[^JeffSnitzer].

## 10. DO provide idempotence mechanisms

```
# GOOD
POST /products
X-Idempotency-Key: 123
```

[^JeffSnitzer]: [How to (and how not to) design REST APIs](https://github.com/stickfigure/blog/wiki/How-to-(and-how-not-to)-design-REST-APIs), Jeff Snitzer
[^JsonVuln]: [Anatomy of a Subtle JSON Vulnerability](https://haacked.com/archive/2008/11/20/anatomy-of-a-subtle-json-vulnerability.aspx/), Haacked