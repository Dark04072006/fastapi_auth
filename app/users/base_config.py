from app.core.settings import config
from fastapi_users.authentication import BearerTransport, JWTStrategy

bearer_transport = BearerTransport(tokenUrl="/auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=config.secret.jwt_secret, lifetime_seconds=3600)
