from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter()


@router.get("/health")
def health_check() -> Response:
    return Response(status_code=200)
