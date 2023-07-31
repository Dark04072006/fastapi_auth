# from fastapi import Depends, Request
# from sqlalchemy.ext.asyncio import AsyncSession

# from app.auth.services import crud_operations
# from core.database.utils import get_session


# async def only_current_user_perm(
#         session: AsyncSession = Depends(get_session), request: Request):
#     token = request.headers.get('Authorization').split()[1]
    
