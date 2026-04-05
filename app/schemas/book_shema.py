from pydantic import BaseModel, Field, field_validator
from decimal import Decimal

class BookRequests(BaseModel):
    name: str = Field(..., max_length=255)
    author: str = Field(..., max_length=255)
    year: str = Field(..., max_length=255)
    cost: Decimal = Field(max_digits=10, decimal_places=2)


    @field_validator("name")
    def book_name_not_empty(cls, v:str) -> str:
        v = v.strip()

        if not v:
            raise ValueError("Book name cannot be empty")
        
        return v


    @field_validator("cost")
    def cost_must_be_positive(cls, v: Decimal) -> Decimal:
        if v <= 0.0:
            raise ValueError("Cost must be positive")
        return v
        