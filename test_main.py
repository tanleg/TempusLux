from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_watches():
    response = client.get("/watches")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_watch():
    response = client.post("/watches", json={
        "name": "Test Watch",
        "brand_id": 1,
        "category_id": 1,
        "price": 1000.00,
        "description": "A test watch",
        "image_url": "http://example.com/watch.jpg"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Test Watch"

def test_get_watch_not_found():
    response = client.get("/watches/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Watch not found"
