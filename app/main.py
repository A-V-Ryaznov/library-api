from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
import uvicorn

from app.api.v1.books import router as books_router

app = FastAPI()

app.include_router(books_router, prefix="/api/v1", tags=["book"])