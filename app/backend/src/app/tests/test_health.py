from fastapi.testclient import TestClient

from app.main import app


def test_ping_endpoint() -> None:
    client = TestClient(app)
    response = client.get("/api/health/ping")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "pong"}
