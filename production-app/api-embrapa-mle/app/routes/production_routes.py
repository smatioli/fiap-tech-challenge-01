from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from app.services.production_service import ProductionService
from app.routes.depends import get_db_session, auth
from datetime import datetime
from fastapi import status
from app.schemas.error import ErrorResponse
from app.schemas.production import ProductionResponse
from typing import List


router = APIRouter(dependencies=[Depends(auth)])


@router.get("/producao", response_model=List[ProductionResponse], responses={
    400: {"model" : ErrorResponse},
    404: {"model" : ErrorResponse}
})
def get_production(
    ano: int = Query(
        default= datetime.now().year - 2,
        description="Ano para o qual os dados de produção são solicitados"
    ),     
    db: Session = Depends(get_db_session)
):  
    """
    Endpoint para obter dados de produção de vinhos, sucos e derivados do Rio Grande do Sul, com base no ano especificado.

    Parâmetros:
    - **ano**: Ano de referência para os dados.
    """

    last_year = datetime.now().year - 2
    if ano < 1970 or ano > last_year:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid year. The year must be between 1970 and {last_year}.")

    ps = ProductionService(db_session=db)
    response = ps.list_production(ano=ano)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No data found for the requested year.")
    return response
