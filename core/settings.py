from decouple import config


JWT_SECRET: str = config("SECRET")
JWT_ALGORITHM: str = config("ALGORITHM")

DATABASE_URL: str = config("DATABASE_URL")

ORIGINS: list = config("ORIGINS").split(',')
ALLOWED_METHODS: list = config("ALLOWED_METHODS").split(',')
ALLOWED_HEADERS: list = config("ALLOWED_HEADERS").split()
