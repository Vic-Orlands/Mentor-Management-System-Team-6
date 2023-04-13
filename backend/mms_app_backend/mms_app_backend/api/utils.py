from typing import TypedDict

from pydantic import BaseModel

from ..configs.database_config import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ResponseModel(BaseModel):
    success: bool = False
    data: dict | None
    message: str | None


class EmptyDict(TypedDict):
    pass