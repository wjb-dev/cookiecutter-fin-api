def test_healthz_endpoint(client):
    resp = client.get("/healthz")
    assert resp.status_code == 200
    payload = resp.json()
    assert payload["service"] == "{{ cookiecutter.project_slug }}"
    assert payload["status"] == "ok"
    assert "version" in payload
