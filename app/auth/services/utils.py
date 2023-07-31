from sqlalchemy import insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.services.password import hash_password
from app.models import User
from app.schemas import UserRegisterSchema


def _get_values(schema: UserRegisterSchema) -> dict:
    return dict(first_name=schema.first_name,
                last_name=schema.last_name,
                email=schema.email,
                password=hash_password(schema.password))


async def _commit_and_return_obj(session: AsyncSession, queryset) -> object:
    await session.commit()
    return queryset.scalar_one()


async def create_user_service(session: AsyncSession, schema: UserRegisterSchema) -> User:
    result = await session.execute(insert(User).values(**_get_values(schema)).returning(User))
    return await _commit_and_return_obj(session, result)


async def update_user_service(session: AsyncSession, email: str, schema: UserRegisterSchema) -> User:
    result = await session.execute(update(User).where(User.email == email).values(**_get_values(schema)).returning(User))
    return await _commit_and_return_obj(session, result)
