from fastapi import FastAPI
from starlette.responses import RedirectResponse

from src.app.routers import game_tokens_router, main_router

app = FastAPI()
app.include_router(main_router.router)
app.include_router(game_tokens_router.router)

