from pydantic import BaseModel
from typing import List


class ImportationResponse(BaseModel):
    pais: str
    quantidade: int
    valor: int

    class Config:
        orm_mode = True