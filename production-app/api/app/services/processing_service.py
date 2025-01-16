from sqlalchemy.orm import Session
from app.db.models import ProcessingDB
from app.schemas.processing import ProcessingResponse
from fastapi.exceptions import HTTPException
from fastapi import status

class ProcessingService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def list_processing(self, ano: int, opcao: str):
        option = self.get_option(opcao)

        if option is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid option.')
        
        processing_lst = self.db_session.query(ProcessingDB).filter(ProcessingDB.year == ano, ProcessingDB.grape_classification == option).all()
        processing_output = [
            self.serialize_processing(processing_model) for processing_model in processing_lst
        ]
        return processing_output
    
    def serialize_processing(self, processing_model: ProcessingDB):
        return ProcessingResponse(
            cultivar = processing_model.grape_cultivar,
            quantidade = processing_model.quantity
        )
    
    def get_option(self, option: str):
        options = {
            'viniferas' : 'Viníferas',
            'americanas_e_hibridas' : 'Americanas e Híbridas',
            'uvas_de_mesa' : 'Uvas de Mesa',
            'sem_classificacao' : 'Sem Classificação'
        }

        return options.get(option, None)
