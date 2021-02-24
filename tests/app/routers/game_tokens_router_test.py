from fastapi.testclient import TestClient

from src.app.main import app

client = TestClient(app)

def test_display_game_tokens():
    response = client.get("/game-tokens/")

    assert response.status_code == 200
    assert response.json() == [{"token": "1233"}, {"token": "1234"}]