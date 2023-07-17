from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend
from app.users.base_config import get_jwt_strategy, bearer_transport
from app.users.manager import get_user_manager
from app.users.models import User

auth_backend = AuthenticationBackend(
    name='jwt',
    transport=bearer_transport,
    get_strategy=get_jwt_strategy
)

fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

current_user = fastapi_users.current_user(active=True)
