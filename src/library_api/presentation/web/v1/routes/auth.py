import secrets

from fastapi import APIRouter, Depends, HTTPException, status

from typing import Annotated
from fastapi.security import HTTPBasic, HTTPBasicCredentials

router = APIRouter()

security = HTTPBasic()


basic_auth_data = {
    "test": "test"
}

def check_auth_user(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        headers={"WWW-Authenticate": "Basic"}
    )

    correct_password = basic_auth_data.get(credentials.username)

    if correct_password is None:
        raise unauthed_exc
    
    if not secrets.compare_digest(
        credentials.password.encode("utf-8"),
        correct_password.encode("utf-8")
    ):
        raise unauthed_exc

    return credentials.username


@router.get("/basic-auth")
def basic_auth( 
    username: str = Depends(check_auth_user)
):
    return{
        "message": f"Hi {username}",
        "username": username
    }

@router.get("/jwt-auth")
def basic_auth( 
    username: str = Depends(check_auth_user)
):
    return{
        "message": f"Hi {username}",
        "username": username
    }