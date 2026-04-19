from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, HTTPException, Request

from library_api.application.users.create import CreateNewUserInteractor
from library_api.application.users.get_all import GetAllUsersInteractor
from library_api.dtos.user import UserDTO, NewUserDTO

router = APIRouter()


@router.get("/users", response_model=list[UserDTO])
@inject
async def get_all_users(request: Request, interactor: FromDishka[GetAllUsersInteractor]):
    return await interactor()


@router.post("/user", response_model=UserDTO)
@inject
async def create_book(
    request: Request, body: NewUserDTO, interactor: FromDishka[CreateNewUserInteractor]
):
    return await interactor(body)
