from fastapi import APIRouter

router = APIRouter()

@router.get("/game-tokens/", name="read_game_tokens", tags=["game_tokens"])
async def read_game_tokens():
    return [{"token": "1233"}, {"token": "1234"}]
