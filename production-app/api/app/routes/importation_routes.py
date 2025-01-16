from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from app.services.importation_service import ImportationService
from app.routes.depends import get_db_session, auth
from datetime import datetime
from fastapi import status
from app.schemas.importation import ImportationResponse
from app.schemas.error import ErrorResponse
from typing import List, Literal

router = APIRouter(dependencies=[Depends(auth)])


@router.get("/importacao", response_model=List[ImportationResponse], responses={
    400: {"model" : ErrorResponse},
    404: {"model" : ErrorResponse}
})
def get_importation(
    ano: int = Query(
        default= datetime.now().year - 2,
        description="Ano para o qual os dados de importação são solicitados"
    ),  
    opcao: Literal[
        "vinhos_de_mesa", 
        "espumantes", 
        "uvas_frescas",
        "uvas_passas",
        "suco_de_uva"
    ] = Query(
        default="vinhos_de_mesa",
        description="Derivado de uva"
    ),
    db: Session = Depends(get_db_session)
):
    """
    Endpoint para obter dados de importação com base no ano e no derivado de uva especificados.

    Parâmetros:
    - **ano**: Ano de referência para os dados.
    - **opcao**: Derivado de uva.
    """

    last_year = datetime.now().year - 2
    if ano < 1970 or ano > last_year:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid year. The year must be between 1970 and {last_year}.")
   
    es = ImportationService(db_session=db)
    response = es.list_importation(ano=ano, opcao=opcao)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No data found for the requested option or year.")
    return response