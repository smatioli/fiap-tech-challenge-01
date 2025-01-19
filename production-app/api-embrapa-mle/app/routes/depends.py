from fastapi import Depends
from app.db.connection import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.services.user_service import UserService

oauth_scheme = OAuth2PasswordBearer(tokenUrl='/usuario/login')

# uma sessao para cada requisicao
def get_db_session():
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()


def auth(
    db_session: Session = Depends(get_db_session),
    token = Depends(oauth_scheme)
):
    us = UserService(db_session=db_session)
    us.verify_token(token=token)