from app.db.base import Base
from app.db.models import ProductionDB, ProcessingDB, CommercializationDB, ImportationDB, ExportationDB, UserDB
from app.db.session import engine

Base.metadata.create_all(bind=engine)