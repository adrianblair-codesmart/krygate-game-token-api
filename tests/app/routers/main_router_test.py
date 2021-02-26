from fastapi.testclient import TestClient

from src.app.main import app

client = TestClient(app)

def test_display_home():
    response = client.get("/")

    assert response.url == f"{client.base_url}/game-tokens/"
    assert response.history[0].is_redirect
    assert response.status_code == 200