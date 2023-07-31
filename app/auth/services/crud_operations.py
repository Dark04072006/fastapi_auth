from typing import Optional
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, insert, update, func

from app.models import User
from app.schemas import UserRegisterSchema
from app.auth.services.password import hash_password


async def get_user_by_email(session: AsyncSession, email: str) -> Optional[User]:
    result = await session.execute(select(User).where(User.email == email))
    result = result.scalar_one_or_none()
    if result is None:
        raise HTTPException(404, 'User does not exists')
    return result


async def create_user(session: AsyncSession, schema: UserRegisterSchema) -> User:
    user = await get_user_by_email(session, email=schema.email)
    if user:
        raise HTTPException(400, "User already exists")
    result = await session.execute(insert(User).values(
                first_name=schema.first_name,
                last_name=schema.last_name,
                email=schema.email,
                password=hash_password(schema.password)
            ).returning(User))
    await session.commit()
    return result.scalar_one()


async def update_user(session: AsyncSession, email: str, schema: UserRegisterSchema) -> User:
    result = await session.execute(update(User).where(User.email == email).values(
                first_name=schema.first_name,
                last_name=schema.last_name,
                email=schema.email,
                password=hash_password(schema.password)
            ).returning(User).returning(User))
    await session.commit()
    return result.scalar_one()


async def delete_user(session: AsyncSession, email: str) -> None:
    await get_user_by_email(session, email)
    await session.execute(delete(User).where(User.email == email))
    await session.commit()
    