from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from app.services.commercialization_service import CommercializationService
from app.routes.depends import get_db_session, auth
from datetime import datetime
from fastapi import status
from app.schemas.error import ErrorResponse
from app.schemas.commercialization import CommercializationResponse
from typing import List

router = APIRouter(dependencies=[Depends(auth)])

@router.get("/comercializacao", response_model=List[CommercializationResponse], responses={
    400: {"model" : ErrorResponse},
    404: {"model" : ErrorResponse}
})
def get_commercialization(
    ano: int = Query(
        default= datetime.now().year - 2,
        description="Ano para o qual os dados de comercialização são solicitados"
    ),      
    db: Session = Depends(get_db_session)
):
    """
    Endpoint para obter dados sobre a comercialização de vinhos e derivados no estado do Rio Grande do Sul, 
    com base no ano de referência fornecido.
    
    Parâmetros:
    - **ano**: Ano de referência para os dados.
    """

    last_year = datetime.now().year - 2
    if ano < 1970 or ano > last_year:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid year. The year must be between 1970 and {last_year}.")
   
    cs = CommercializationService(db_session=db)
    response = cs.list_commercialization(ano=ano)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No data found for the requested year.")
    return response