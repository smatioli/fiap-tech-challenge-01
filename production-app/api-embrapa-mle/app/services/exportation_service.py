from sqlalchemy.orm import Session
from app.db.models import ExportationDB
from app.schemas.exportation import ExportationResponse
from fastapi.exceptions import HTTPException
from fastapi import status

class ExportationService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def list_exportation(self, ano: int, opcao: str):
        option = self.get_option(opcao)

        if option is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid option.')
        
        exportation_lst = self.db_session.query(ExportationDB).filter(ExportationDB.year == ano, ExportationDB.grape_derivative == option).all()
        exportation_output = [
            self.serialize_exportation(exportation_model) for exportation_model in exportation_lst
        ]
        return exportation_output
    
    def serialize_exportation(self, exportation_model: ExportationDB):
        return ExportationResponse(
            pais = exportation_model.country,
            quantidade = exportation_model.quantity,
            valor = exportation_model.value
        )
    
    def get_option(self, option: str):
        options = {
            'vinhos_de_mesa' : 'Vinhos de Mesa',
            'espumantes' : 'Espumantes',
            'uvas_frescas' : 'Uvas Frescas',           
            'suco_de_uva' : 'Suco de Uva'
        }

        return options.get(option, None)
