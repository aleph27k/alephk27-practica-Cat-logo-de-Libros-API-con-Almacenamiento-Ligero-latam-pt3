from tinydb import Query

from app.database import books_table, db_lock
from app.models.book import Book, BookCreate, Genre, Status


def _to_book(doc) -> Book:
    return Book(id=doc.doc_id, **doc)


def create(data: BookCreate) -> Book:
    payload = data.model_dump(mode="json")
    with db_lock:
        doc_id = books_table.insert(payload)
    return Book(id=doc_id, **payload)


def list_all(genre: Genre | None = None, status: Status | None = None) -> list[Book]:
    q = Query()
    conditions = []
    if genre:
        conditions.append(q.genre == genre.value)
    if status:
        conditions.append(q.status == status.value)

    with db_lock:
        if not conditions:
            docs = books_table.all()
        else:
            cond = conditions[0]
            for c in conditions[1:]:
                cond &= c
            docs = books_table.search(cond)
    return [_to_book(d) for d in docs]


def get(book_id: int) -> Book | None:
    with db_lock:
        doc = books_table.get(doc_id=book_id)
    return _to_book(doc) if doc else None


def update_status(book_id: int, status: Status) -> Book | None:
    with db_lock:
        if not books_table.contains(doc_id=book_id):
            return None
        books_table.update({"status": status.value}, doc_ids=[book_id])
        doc = books_table.get(doc_id=book_id)
    return _to_book(doc)


def delete(book_id: int) -> bool:
    with db_lock:
        if not books_table.contains(doc_id=book_id):
            return False
        books_table.remove(doc_ids=[book_id])
    return True


def exists(title: str, author: str) -> bool:
    q = Query()
    with db_lock:
        return books_table.contains((q.title == title) & (q.author == author))
