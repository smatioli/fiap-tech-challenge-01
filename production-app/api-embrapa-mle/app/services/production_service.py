from sqlalchemy.orm import Session
from app.db.models import ProductionDB
from app.schemas.production import ProductionResponse


class ProductionService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def list_production(self, ano: int):
        production_lst = self.db_session.query(ProductionDB).filter_by(year=ano)
        production_output = [
            self.serialize_production(production_model) for production_model in production_lst
        ]
        return production_output
    
    def serialize_production(self, production_model: ProductionDB):
        return ProductionResponse(
            produto=production_model.product,
            quantidade = production_model.quantity
        )