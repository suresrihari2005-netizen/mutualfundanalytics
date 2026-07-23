from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "Running"


def test_cluster_labels():
    response = client.get("/cluster-labels")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
