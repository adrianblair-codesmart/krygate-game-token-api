from fastapi import APIRouter, Depends
from src.app import dependencies
from src.app.config.settings import Settings
from src.game_token.game_token import GameToken

router = APIRouter(
    prefix="/game-tokens",
    tags=["game-tokens"],
    dependencies=[Depends(dependencies.get_settings)],
    # responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_all_game_tokens():
    return [{"token": "1233"}, {"token": "1234"}]


@router.get("/{game_token_id}")
async def get_game_token(game_token_id: str):
    return game_token_id


@router.post("/")
async def create_game_token(game_token: GameToken) -> GameToken:
    return GameToken(**{
        "game_token_id": "the id for this token.",
        "game_token_name": "this is a new token.",
        "game_token_key": "this is a new token key.",
        "allowed_domains": ["bits-and-bobs.com"]
    })


@router.put("/{game_token_id}")
async def update_game_token(game_token_id: str, game_token: GameToken) -> GameToken:
    return GameToken(**{
        "game_token_id": "the id for this token.",
        "game_token_name": "this is a new token.",
        "game_token_key": "this is a new token key.",
        "allowed_domains": ["bits-and-bobs.com"]
    })

@router.delete("/{game_token_id}")
async def update_game_token(game_token_id: str) -> bool:
    return True