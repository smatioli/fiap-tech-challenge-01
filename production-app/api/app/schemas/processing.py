from pydantic import BaseModel
from typing import List


class ProcessingResponse(BaseModel):
    cultivar: str
    quantidade: int

    class Config:
        orm_mode = True