from fastapi import APIRouter
from starlette.responses import RedirectResponse

router = APIRouter()

@router.get("/", tags=["main"])
async def display_home():
    response = RedirectResponse(url='/game-tokens/')
    return response