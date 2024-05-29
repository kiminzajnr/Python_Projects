# Simple REST API

==========================================

## Features

- Create stores, each with a `name` and a list of stocked `items`.
- Create an item within a `store`, each with a `name` and a `price`.
- Retrieve a list of all stores and their items.
- Given its `name`, retrieve an individual store and all its items.
- Given a store `name`, retrieve only a list of item within it.

## Create stores

Request:
```
POST /store {"name": "My Store"}
```

Response:
```
{"name": "My Store", "items": []}
```

## Create items

Request:
```
POST /store/My Store/item {"name": "Chair", "price": 175.50}
```
Response:
```
{"name": "Chair", "price": 175.50}
```

## Retrieve all stores and their items

Request:
```
GET /store
```
Response:
```
{
    "stores": [
        {
            "name": "My Store",
            "items": [
                {
                    "name": "Chair",
                    "price": 175.50
                }
            ]
        }
    ]
}
```

## Get only items in a store

Request:
```
GET /store/My Store/item
```
Response:
```
[
    {
        "name": "Chair",
        "price": 175.50
    }
]
```