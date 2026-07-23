from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "Running"
    assert "message" in data


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "Healthy"}


def test_cluster_labels():
    response = client.get("/cluster-labels")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_portfolio_stats():
    response = client.get("/portfolio-stats")

    assert response.status_code == 200
    assert isinstance(response.json(), list)