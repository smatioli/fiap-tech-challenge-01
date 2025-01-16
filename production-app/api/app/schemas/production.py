from pydantic import BaseModel
from typing import List

class ProductionResponse(BaseModel):
    produto: str
    quantidade: int

    class Config:
        orm_mode = True