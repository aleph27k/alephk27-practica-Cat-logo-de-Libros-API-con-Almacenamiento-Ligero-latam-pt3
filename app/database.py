from pathlib import Path
from threading import Lock

from tinydb import TinyDB

DB_PATH = Path(__file__).resolve().parent.parent / "db.json"

db = TinyDB(DB_PATH, indent=2, ensure_ascii=False)
books_table = db.table("books")

# TinyDB is not thread-safe and FastAPI runs sync endpoints in a thread pool.
db_lock = Lock()
