from pydantic import BaseModel
from typing import List


class ExportationResponse(BaseModel):
    pais: str
    quantidade: int
    valor: int

    class Config:
        orm_mode = True