# Project 1 : FastAPI Request Method Logic

from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title' : 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'},
]

# CRUD (Create, Read, Update Delete)
# HTTP Request (Post, Get, Put, Delete)

@app.get("/books")
async def read_all_books():
    return BOOKS


# @app.get("/books/mybook")
# async def read_all_books():
#     return {'book_title': 'My favorite book!'}


@app.get("/books/{book_title}")
# request with GET cannot have Body
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        return None
    return None
# can pass in anything inside dynamic_param (for example science)

# @app.get("/books/mybook")
# async def read_all_books():
#     return {'book_title': 'My favorite book!'}
# #if this code snippet after dynamic param
# #it still calls as dynamic_param. Order matters!


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return
# searches by category (for example, science)

# Query Parameter (ORDER MATTERS)
@app.get("/books/byauthor/")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# POST Request
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
# Body = [{“title”: “Title Seven”, “author”: “Author Two”, “category”: “math”}]

# PUT Request Method
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

# DELETE Request
@app.delete("/books/delete_book")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

# create new API endpoint that can fetch all books from a specific author using either path parameters or query parameters
# Path parameter
@app.get("/books/byauthor/{author}")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return

