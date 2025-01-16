from fastapi import status, Response, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.routes.depends import get_db_session
from app.schemas.user import User
from app.services.user_service import UserService
from app.schemas.error import ErrorResponse


router = APIRouter(prefix='/usuario')

@router.post('/cadastrar', response_class=Response, status_code=status.HTTP_201_CREATED, responses={
    404: {"model" : ErrorResponse}
})
def user_register(
    user: User,
    db_session: Session = Depends(get_db_session)
):
    """
    Endpoint para registrar um novo usuário.

    - **user**: Objeto que contém as informações do usuário (nome de usuário e senha).
    """

    us = UserService(db_session=db_session)
    us.register_user(user=user)
    return Response(status_code=status.HTTP_201_CREATED)


@router.post('/login', responses={
    401: {"model" : ErrorResponse}
})
def user_login(
    login_request_form: OAuth2PasswordRequestForm = Depends(),
    db_session: Session = Depends(get_db_session)
):
    """
    Endpoint para realizar o login e obter um token JWT, que deve ser usado para autenticação nas requisições.

    Parâmetros:
     - **login_request_form**: Formulário com o nome de usuário e senha.
    """

    us = UserService(db_session=db_session)

    user = User(
        username=login_request_form.username,
        password=login_request_form.password
    )

    token_data = us.user_login(user=user, expires_in=60)

    return token_data