from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar('T')


class Reponse(BaseModel, Generic[T]):
    data: Optional[T] = None
    message: str
