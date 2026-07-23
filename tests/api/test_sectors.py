from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_api_running():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "Running"
