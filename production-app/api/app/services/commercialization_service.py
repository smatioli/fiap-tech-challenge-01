from sqlalchemy.orm import Session
from app.db.models import CommercializationDB
from app.schemas.commercialization import CommercializationResponse


class CommercializationService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def list_commercialization(self, ano: int):
        commercialization_lst = self.db_session.query(CommercializationDB).filter_by(year=ano)
        commercialization_output = [
            self.serialize_commercialization(commercialization_model) for commercialization_model in commercialization_lst
        ]
        return commercialization_output
    
    def serialize_commercialization(self, commercialization_model: CommercializationDB):
        return CommercializationResponse(
            produto=commercialization_model.product,
            quantidade = commercialization_model.quantity
        )