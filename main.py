from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.views.book_routes import router as books_router
from seed import seed


@asynccontextmanager
async def lifespan(app: FastAPI):
    count = seed()
    print(f"Seed al arrancar: {count} registro(s) insertado(s).")
    yield


app = FastAPI(title="Catálogo de Libros", lifespan=lifespan)
app.include_router(books_router)
