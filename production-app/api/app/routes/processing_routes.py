from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Literal
from sqlalchemy.orm import Session
from app.services.processing_service import ProcessingService
from app.routes.depends import get_db_session, auth
from datetime import datetime
from fastapi import status
from app.schemas.processing import ProcessingResponse
from app.schemas.error import ErrorResponse


router = APIRouter(dependencies=[Depends(auth)])


@router.get("/processamento", response_model=List[ProcessingResponse], responses={
    400: {"model" : ErrorResponse},
    404: {"model" : ErrorResponse}
})
def get_processing(
    ano: int = Query(
        default= datetime.now().year - 2,
        description="Ano para o qual os dados de processamento são solicitados"
    ),  
    opcao: Literal[
        "viniferas", 
        "americanas_e_hibridas", 
        "uvas_de_mesa", 
        "sem_classificacao"
    ] = Query(
        default="viniferas",
        description="Categoria de processamento"
    ),
    db: Session = Depends(get_db_session) 
):
    """
    Endpoint para obter dados de processamento com base no ano e categoria especificados.

    Parâmetros:
    - **ano**: Ano de referência para os dados.
    - **opcao**: Categoria de processamento.
    """

    last_year = datetime.now().year - 2
    if ano < 1970 or ano > last_year:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid year. The year must be between 1970 and {last_year}.")
   
    ps = ProcessingService(db_session=db)
    response = ps.list_processing(ano=ano, opcao=opcao)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No data found for the requested option or year.")
    return response