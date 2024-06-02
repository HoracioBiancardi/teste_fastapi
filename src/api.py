# api.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    """Rota principal

    Returns:
        dict: Hello, World
    """
    return {"message": "Hello, World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None) -> dict:
    """Rota de ge items

    Args:
        item_id (int): id do item
        q (str, optional): _description_. Defaults to None.

    Returns:
        dict: item_id
    """
    return {"item_id": item_id, "q": q}
