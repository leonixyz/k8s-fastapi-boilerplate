from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/api/items")
def read_root():
    return [
        {
            "id": "1",
            "title": "One",
            "icon": "github",
            "descr": "Lorem Ipsum Dolor Sit Amet"
        },
        {
            "id": "2",
            "title": "Two",
            "icon": "cellphone-link",
            "descr": "Quo atque totam aut a voluptas"
        },
        {
            "id": "3",
            "title": "Three",
            "icon": "alert-decagram",
            "descr": "Ut omnis architecto sit perferendis"
        },
        {
            "id": "4",
            "title": "Four",
            "icon": "arrange-bring-to-front",
            "descr": "Reprehenderit iste similique culpa"
        }
    ]


@app.get("/api/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}