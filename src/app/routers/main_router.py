from fastapi import APIRouter, Depends
from starlette.responses import RedirectResponse
from src.app import dependencies
from src.app.config.settings import Settings

router = APIRouter(
    tags=["main"]
)


@router.get("/")
async def display_home():
    response = RedirectResponse(url='/game-tokens/')
    return response
