from fastapi.testclient import TestClient

from src.app.main import app
from src.game_token.game_token import GameToken

client = TestClient(app)


def test_get_all_game_tokens():
    response = client.get("/game-tokens/")

    assert response.status_code == 200
    assert response.json() == [{"token": "1233"}, {"token": "1234"}]


def test_create_game_token(game_token_without_id: GameToken, game_token_with_id: GameToken):
    response = client.post("/game-tokens/", game_token_without_id.json())
    assert response.json() == game_token_with_id


def test_update_game_token(game_token_without_id: GameToken, game_token_with_id: GameToken):
    response = client.put(f"/game-tokens/{game_token_with_id.game_token_id}", game_token_without_id.json())
    assert response.json() == game_token_with_id

def test_delete_game_token(game_token_with_id: GameToken):
    response = client.delete(f"/game-tokens/{game_token_with_id.game_token_id}")

    assert response.status_code == 204