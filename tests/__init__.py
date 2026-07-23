import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_cluster_labels():
    response = client.get("/cluster-labels")
    assert response.status_code == 200


def test_portfolio_stats():
    response = client.get("/portfolio-stats")
    assert response.status_code == 200