from app.models import book_repository as repo
from app.models.book import BookCreate

SEED_BOOKS = [
    {"title": "The Pragmatic Programmer", "author": "Hunt & Thomas",  "genre": "non-fiction", "pages": 352, "status": "available"},
    {"title": "Dune",                     "author": "Frank Herbert",  "genre": "sci-fi",      "pages": 412, "status": "available"},
    {"title": "The Big Sleep",            "author": "Raymond Chandler","genre": "mystery",    "pages": 231, "status": "checked_out"},
    {"title": "Nineteen Eighty-Four",     "author": "George Orwell",  "genre": "fiction",     "pages": 328, "status": "available"},
]


def seed() -> int:
    inserted = 0
    for raw in SEED_BOOKS:
        book = BookCreate(**raw)
        # (title, author) acts as the natural key to keep the seeder idempotent.
        if repo.exists(book.title, book.author):
            continue
        repo.create(book)
        inserted += 1
    return inserted


if __name__ == "__main__":
    count = seed()
    print(f"Seed completado: {count} registro(s) insertado(s).")
