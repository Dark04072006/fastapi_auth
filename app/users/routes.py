from fastapi import APIRouter
from app.users.auth_backend import auth_backend, fastapi_users
from app.users.schemas import UserRead, UserCreate


router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['Авторизация']
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['Авторизация']
)

router.include_router(fastapi_users.get_users_router(
    UserRead, UserCreate
), prefix='/users', tags=['users'])
