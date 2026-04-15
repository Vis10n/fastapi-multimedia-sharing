from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)


def test_hello_world_status_code():
    response = client.get("/hello-world")
    assert response.status_code == 200


def test_hello_world_response():
    response = client.get("/hello-world")
    assert response.json() == {"message": "Hello World!"}
