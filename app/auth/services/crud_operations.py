from typing import Optional
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from app.models import User
from app.schemas import UserRegisterSchema
from app.auth.services.utils import create_user_service, update_user_service


async def get_user_by_email(session: AsyncSession, email: str) -> Optional[User]:
    result = await session.execute(select(User).where(User.email == email))
    result = result.scalar_one_or_none()
    return result


async def create_user(session: AsyncSession, schema: UserRegisterSchema) -> User:
    user = await get_user_by_email(session, email=schema.email)
    if user:
        raise HTTPException(400, "User already exists")
    return await create_user_service(session, schema)


async def update_user(session: AsyncSession, email: str, schema: UserRegisterSchema) -> User:
    return await update_user_service(session, email, schema)


async def delete_user(session: AsyncSession, email: str) -> None:
    await get_user_by_email(session, email)
    await session.execute(delete(User).where(User.email == email))
    await session.commit()
