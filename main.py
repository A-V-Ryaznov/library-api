from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
import uvicorn

app = FastAPI()

BOOKS = {
    "Pomadoro": ["Frank", "1990"],
    "Dune": ["Herbert", "1950"]
}


@app.get("/health")
def health_check():
    return Response(status_code=200)

@app.get("/books")
def get_books():
    return BOOKS


@app.get("/books/{name}")
def get_book(book_name: str | None = None):
    if book_name is None:
          raise HTTPException(
            status_code = 404,
            detail=f"Book_name is empty"
        )
    if book_name not in BOOKS:
        raise HTTPException(
            status_code = 404,
            detail=f"Book '{book_name}' not found"
        )
    
    return BOOKS[book_name]

@app.post("/book/{name}")
def add_book(name: str, author: str, year: str):
    
    if name in BOOKS:
        raise HTTPException(
            status_code= 404,
            detail=f"Book {name} already exiest"
        )
    
    BOOKS[name] = [author, year]

    return {
        "name": name,
        "author": author,
        "year": year
    }


def run() -> None:
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8282,
        log_level="trace"
    )

if __name__ == "__main__":
    run()