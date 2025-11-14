from app import app
import json

def test_home():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200

def test_add_and_get():
    client = app.test_client()
    r = client.post("/todos", json={"task":"test1"})
    assert r.status_code == 201
    r2 = client.get("/todos")
    data = json.loads(r2.data)
    assert any(t["task"] == "test1" for t in data)
