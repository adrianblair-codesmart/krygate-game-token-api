from typing import Optional
from pydantic.main import BaseModel


class GameToken(BaseModel):
    game_token_id: Optional[str]
    game_token_name: str
    game_token_key: str
    allowed_domains: Optional[list[str]] = []
