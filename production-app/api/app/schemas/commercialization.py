from pydantic import BaseModel
from typing import List


class CommercializationResponse(BaseModel):
    produto: str
    quantidade: int

    class Config:
        orm_mode = True