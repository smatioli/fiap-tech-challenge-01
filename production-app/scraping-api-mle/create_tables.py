from app.db.base import Base
from app.db.connection import engine
from app.db.models import *

def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
    print("Tables created successfully!") 