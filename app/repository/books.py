from typing import Final

from decimal import Decimal

BOOKS: Final[dict[str, list[str, str, Decimal]]] = {
    "Pomadoro": ["Frank", "1990", Decimal("500.82")],
    "Dune": ["Herbert", "1950", Decimal("300.64")]
}

def get_all_books() -> dict[str, str, str, Decimal]:
    return BOOKS.copy()

def is_book_exist(book_name: str) -> bool:
    return book_name in BOOKS

def add_book(book_name: str, book_author: str, book_year: str, book_cost: Decimal) -> None:
    BOOKS[book_name] += [book_author, book_year, book_cost]
    return