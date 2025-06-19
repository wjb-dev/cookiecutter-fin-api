from fastapi.testclient import TestClient
from src.python.main import app

client = TestClient(app)

def test_health():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json()["service"] == "{{ cookiecutter.project_slug }}"
    assert r.json()["status"] == "ok"
