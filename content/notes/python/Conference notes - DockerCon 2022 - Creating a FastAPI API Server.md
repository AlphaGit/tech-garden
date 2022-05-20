---
title: Conference notes: Quickly Creating a Production-Ready API Using FastAPI and Docker…Explained with Memes
tags:
- conference
- docker
- dockercon
- fastapi
- python
- api
- dockercon2022
---

Notes from https://docker.events.cube365.net/dockercon/2022/content/Videos/FznJCYerdb9Za3W9Q

Based on OpenAPI, JSON, OAuth2, generates automatic API docs.

Based on python type hints, FastAPI uses it.

```python
class Item(BaseModel):
   name: str

@app.post("/items/")
async def create_item(item: Item):
    return ...
```

This provides autocompletion in the IDE, also JSON type checks.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# https://somedomain.com/items/5?q=some+query
```

Because `q` is not defined in the path, it becomes part of the query parameters.

Going to `/docs` will give you the Swagger interface, auto-generated.

```python
from typing import List
from pydantic import BaseModel

class Food(BaseModel):
    name: str
    ingredients: List[str] = []

@app.post("/food/")
def prepare_food(food: Food):
    return {"message": f"preparing {food.name}"}
```

Because the model is not found in the path, it will be retrieved from the POST body.

```python
@app.post("/food/")
def prepare_food(food: Food, delivery: bool = False):
    return ...
```

Because `delivery` is not found between the pydantic models, it will retrieve it from the POST query string. FastAPI will not pass a `string` into our methods, but rather a real `bool` value.

```python
@app.post("/food/")
def prepare_food(orders: List[Food]):
    all_ingredients = []
    for food in orders:
        for ingredient in food.ingredients:
            all_ingredients.append(ingredient.lower())

    return {"ingredients": all_ingredients}
```

The types are again, considered natively and FastAPI does the magic of obtaining a JSON Array as the request body.

`ingredients` was defined with a default of an empty list, meaning that it will not be required. `name` was not, so it will be required.

Sending invalid data (this is, valid JSON but not valid to the schema defined), will return a 422 status code, and it will return detail of the validations that failed.

It will also tells us exactly where the error was (see `detail[].loc`)

```json
{
  "detail": [{
    "loc": [ "body", "orders", 2, "ingredients", 1 ],
    "msg": "str type unexpected",
    "type": "type_error.str"
  }, {
    "loc": [ "body", "orders", 3, "name" ],
    "msg": "field required",
    "type": "value_error.missing"
  }]
}
```

Settign it up in docker:

```docker
FROM python:3.10
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
```

This is all that's needed to setup a FastAPI server for it. This is what you'd normally do if you have Kubernetes or other orchestrators, or if you have a cloud service that runs the services for you.

In some cases, when you're doing manual deployments, manual deployment commands, docker-compose or other cases, you can use this docker image:

```docker
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
COPY ./requirements /app/requirements.tt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./app /app
```

Useful if you need multiple processes inside the same container, like if you can only run a single container. It is generally advisable to use the other option.

More about it in https://fastapi.tiangolo.com/deployment/docker

Other features:

- Dependency injection
- OAuth2
- Websockets
- Files
- Background Tasks
- Easy GraphQL integration

