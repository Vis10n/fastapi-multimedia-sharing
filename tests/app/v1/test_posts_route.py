import pytest

from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.api.v1.routes.posts import router


@pytest.fixture
def client():
    app = FastAPI()
    app.include_router(router)
    return TestClient(app)


def test_get_all_posts(client):
    response = client.get("/posts-configuration/posts?limit=5")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 5


def test_get_post_success(client):
    response = client.get("/posts-configuration/posts/0")
    assert response.status_code == 200

    data = response.json()
    assert "title" in data
    assert "content" in data


def test_get_post_not_found(client):
    response = client.get("/posts-configuration/posts/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Post not found."


def test_create_post(client):
    payload = {"title": "New Post", "content": "This is a new post for testing"}

    response = client.post("/posts-configuration/posts", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["title"] == payload["title"]
    assert data["content"] == payload["content"]
    assert data["word_count"] == len(payload["content"].split())


def test_update_post_success(client):
    payload = {"title": "Updated Title", "content": "Updated content"}

    response = client.put("/posts-configuration/posts/0", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["new_title"] == payload["title"]
    assert data["new_content"] == payload["content"]
    assert "old_title" in data
    assert "old_content" in data


def test_update_post_not_found(client):
    payload = {"title": "Updated Title", "content": "Updated content"}

    response = client.put("/posts-configuration/posts/999", json=payload)
    assert response.status_code == 404
    assert response.json()["detail"] == "Post not found."


def test_delete_post_success(client):
    # Better approach: try deleting known existing id
    response = client.delete("/posts-configuration/posts/0")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 0
    assert "title" in data
    assert "content" in data


def test_delete_post_not_found(client):
    response = client.delete("/posts-configuration/posts/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Post not found."
