from fastapi import APIRouter, Path, Response, status as http_status

from app.controllers import book_controller as ctrl
from app.models.book import Book, BookCreate, Genre, Status, StatusUpdate

router = APIRouter(prefix="/books", tags=["books"])


@router.post("", response_model=Book, status_code=http_status.HTTP_201_CREATED)
def create_book(data: BookCreate):
    return ctrl.create_book(data)


@router.get("", response_model=list[Book])
def list_books(genre: Genre | None = None, status: Status | None = None):
    return ctrl.list_books(genre, status)


@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int = Path(..., gt=0)):
    return ctrl.get_book(book_id)


@router.patch("/{book_id}/status", response_model=Book)
def change_status(data: StatusUpdate, book_id: int = Path(..., gt=0)):
    return ctrl.change_status(book_id, data.status)


@router.delete("/{book_id}", status_code=http_status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int = Path(..., gt=0)):
    ctrl.delete_book(book_id)
    return Response(status_code=http_status.HTTP_204_NO_CONTENT)
