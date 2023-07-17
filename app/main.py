from fastapi import FastAPI
from app.users.routes import router as auth_router
from app.posts.routes import router as posts_router


app = FastAPI(
    title='Блог на FastAPI'
)


app.include_router(auth_router)
app.include_router(posts_router)
