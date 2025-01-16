from sqlalchemy.orm import Session
from app.db.models import ImportationDB
from app.schemas.importation import ImportationResponse
from fastapi.exceptions import HTTPException
from fastapi import status

class ImportationService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def list_importation(self, ano: int, opcao: str):
        option = self.get_option(opcao)

        if option is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid option.')
        
        importation_lst = self.db_session.query(ImportationDB).filter(ImportationDB.year == ano, ImportationDB.grape_derivative == option).all()
        importation_output = [
            self.serialize_importation(importation_model) for importation_model in importation_lst
        ]
        return importation_output
    
    def serialize_importation(self, importation_model: ImportationDB):
        return ImportationResponse(
            pais = importation_model.country,
            quantidade = importation_model.quantity,
            valor = importation_model.value
        )
    
    def get_option(self, option: str):
        options = {
            'vinhos_de_mesa' : 'Vinhos de Mesa',
            'espumantes' : 'Espumantes',
            'uvas_frescas' : 'Uvas Frescas',
            'uvas_passas' : 'Uvas Passas',
            'suco_de_uva' : 'Suco de Uva'
        }

        return options.get(option, None)
