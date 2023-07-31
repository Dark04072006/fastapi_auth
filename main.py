from app.auth.services.password import verify_password
from app.auth.auth_handler import signJWT, verify_jwt, decodeJWT
from app.auth.auth_bearer import JWTBearer
from app.auth.services import crud_operations as service
# from app.auth.permissions import only_current_user_perm

from app import schemas
from app.models import User
from core.database.utils import get_session, init_models
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import FastAPI, HTTPException, Depends, Response, status
from fastapi.responses import JSONResponse


app = FastAPI(title='Сервис авторизации на FastAPI')


@app.on_event("startup")
async def on_startup() -> None:
    await init_models()


@app.post('/api/signup', response_model=schemas.UserSchema, tags=['Авторизация'])
async def register(user: schemas.UserRegisterSchema, session: AsyncSession = Depends(get_session)):
    return await service.create_user(session, user)


@app.post('/api/login', response_model=schemas.TokenSchema, tags=['Авторизация'])
async def login(user: schemas.UserLoginSchema, session: AsyncSession = Depends(get_session)):
    queryset = await service.get_user_by_email(session, user.email)
    if (queryset is None) or (not verify_password(user.password, queryset.password)):
        raise HTTPException(401, status.HTTP_401_UNAUTHORIZED)
    return signJWT(queryset.email)


@app.post('/api/verify-token', tags=['Авторизация'])
async def verify(token: schemas.TokenSchema):
    if verify_jwt(token.access_token):
        return JSONResponse({'message': 'success'}, status.HTTP_200_OK)
    return JSONResponse({'message': 'invalid token'}, status.HTTP_400_BAD_REQUEST)


@app.get('/api/users/me', response_model=schemas.UserSchema, responses={200: {"model": schemas.UserSchema}}, tags=['Пользователь'])
async def get_user(user: User = Depends(JWTBearer())) -> User:
    return user


@app.patch('/api/users/me', response_model=schemas.UserSchema, tags=['Пользователь'])
async def patch_user(schema: schemas.UserRegisterSchema, session: AsyncSession = Depends(get_session), user: User = Depends(JWTBearer())):
    return await service.update_user(session, user.email, schema)


@app.delete('/api/users/me', tags=['Пользователь'])
async def delete_user(session: AsyncSession = Depends(get_session), user: User = Depends(JWTBearer())):
    await service.delete_user(session, user.email)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
