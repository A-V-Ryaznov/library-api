from fastapi import APIRouter, HTTPException, Request

from dishka.integrations.fastapi import inject, FromDishka

from library_api.dtos.book import NewBookDTO, BookDTO
from library_api.application.books.create import CreateNewBookInteractor
from library_api.application.books.get_all import GetAllBooksInteractor
from library_api.application.books.get_by_name import GetBookByNameInteractor
from library_api.exceptions.book import BookNotFound


router = APIRouter()


@router.get("/books", response_model=tuple[BookDTO])
@inject
def get_all_books(request: Request, interactor: FromDishka[GetAllBooksInteractor]):
    return interactor()


@router.get("/books/{name}", response_model=BookDTO)
@inject
def get_book(
    request: Request,
    name: str, 
    interactor: FromDishka[GetBookByNameInteractor]
):
    try:
        return interactor(name)
    except BookNotFound:
        raise HTTPException(
            status_code = 404,
            detail=f"Book '{name}' not found"
        )


@router.post("/book", response_model=BookDTO)
@inject
def create_book(
    request: Request,
    body: NewBookDTO,
    interactor: FromDishka[CreateNewBookInteractor]
):
    return interactor(body)
