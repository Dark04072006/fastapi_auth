from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.core.database import AsyncSession, get_async_session
from sqlalchemy import insert, update, delete, select

from app.posts.models import Post
from app.users.auth_backend import current_user
from app.users.models import User
from app.posts.errors import Message

from app.posts.schemas import Post as PostSchema, PostCreate

router = APIRouter(
    prefix='/posts',
    tags=['Посты']
)


@router.get('/', status_code=200, response_model=list[PostSchema])
async def get_post_list(session: AsyncSession = Depends(get_async_session),
                        user: User = Depends(current_user)):
    result = await session.execute(select(Post))
    return result.all()


@router.get('/{post_id}',
            status_code=200,
            responses={404: {'model': Message}},
            response_model=PostSchema)
async def get_single_post(post_id: int, session: AsyncSession = Depends(get_async_session),
                          user: User = Depends(current_user)):
    result = await session.execute(select(Post).where(Post.id == post_id))
    if result := result.fetchone() is not None:
        return result
    return JSONResponse(status_code=404, content={'message': 'post not found'})
