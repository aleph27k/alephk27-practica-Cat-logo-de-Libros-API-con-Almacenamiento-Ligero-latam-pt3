from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class Genre(str, Enum):
    FICTION = "fiction"
    NON_FICTION = "non-fiction"
    MYSTERY = "mystery"
    SCI_FI = "sci-fi"


class Status(str, Enum):
    AVAILABLE = "available"
    CHECKED_OUT = "checked_out"


class BookCreate(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    genre: Genre
    pages: int = Field(..., gt=0)
    status: Status = Status.AVAILABLE


class StatusUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: Status


class Book(BookCreate):
    id: int
