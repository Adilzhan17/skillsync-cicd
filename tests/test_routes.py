import pytest
from app import create_app

@pytest.fixture()
def client():
    app = create_app()
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client

def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"

def test_jobs(client):
    resp = client.get("/jobs")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list) and len(data) >= 2
    assert all("title" in j and "company" in j for j in data)