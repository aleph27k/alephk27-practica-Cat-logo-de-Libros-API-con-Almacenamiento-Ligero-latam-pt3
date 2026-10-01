from fastapi import HTTPException, status as http_status

from app.models import book_repository as repo
from app.models.book import Book, BookCreate, Genre, Status


def _not_found(book_id: int) -> HTTPException:
    return HTTPException(
        status_code=http_status.HTTP_404_NOT_FOUND,
        detail=f"Book {book_id} not found",
    )


def create_book(data: BookCreate) -> Book:
    return repo.create(data)


def list_books(genre: Genre | None, status: Status | None) -> list[Book]:
    return repo.list_all(genre=genre, status=status)


def get_book(book_id: int) -> Book:
    book = repo.get(book_id)
    if book is None:
        raise _not_found(book_id)
    return book


def change_status(book_id: int, status: Status) -> Book:
    book = repo.update_status(book_id, status)
    if book is None:
        raise _not_found(book_id)
    return book


def delete_book(book_id: int) -> None:
    if not repo.delete(book_id):
        raise _not_found(book_id)
