from fastapi import FastAPI

from function.BookManager import *

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.get("/api/book")
# async def book():
#     return SelectData(query="SELECT * FROM BOOKS_TB")


@app.get("/api/book")
async def book(tag: str = ""):
    return SelectData(query="SELECT * FROM BOOKS_TB",
                      option=f"WHERE INSTR(TAG, '{tag}') AND IS_TAKED = 0")


@app.get("/api/book/{data}")
async def book(data: str):
    return SelectData(query=f"SELECT * FROM BOOKS_TB",
                      option=f"WHERE INSTR(TITLE, '{data}') AND IS_TAKED = 0")


# @app.get("/api/taked_book")
# async def book():
#     return SelectData(query="SELECT * FROM BOOKS_TB",
#                       option=f"WHERE IS_TAKED = 1")


@app.get("/api/taked_book")
async def book(tag: str = ""):
    return SelectData(query="SELECT * FROM BOOKS_TB",
                      option=f"WHERE INSTR(TAG, '{tag}') AND IS_TAKED = 1")


@app.get("/api/taked_book/{data}")
async def book(data: str):
    return SelectData(query=f"SELECT * FROM BOOKS_TB",
                      option=f"WHERE INSTR(TITLE, '{data}') AND IS_TAKED = 1")


@app.get("/api/takeout/{bookId}")
async def update(bookId: str):
    book = SelectData(query=f"SELECT * FROM BOOKS_TB WHERE ID = {bookId}")
    UpdateData(query=f"UPDATE BOOKS_TB SET IS_TAKED = {1 - book[0]['IS_TAKED']} WHERE ID = {bookId}")
    return [{"detail": 1 - book[0]['IS_TAKED']}]


@app.get("/api/removeALL")
async def update():
    UpdateData(query=f"UPDATE BOOKS_TB SET IS_TAKED = 0")
    return [{"detail": 0}]
