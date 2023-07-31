from decouple import config


JWT_SECRET: str = config("SECRET")
JWT_ALGORITHM: str = config("ALGORITHM")

DATABASE_URL: str = config("DATABASE_URL")
