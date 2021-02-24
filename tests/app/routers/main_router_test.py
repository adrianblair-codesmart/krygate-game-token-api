from fastapi.testclient import TestClient

from src.app.main import app

client = TestClient(app)

def test_display_home():
    response = client.get("/")

    assert response.url == client.base_url + app.url_path_for("read_game_tokens")
    assert response.history[0].is_redirect
    assert response.status_code == 200