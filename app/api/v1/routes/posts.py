import logging

from fastapi import APIRouter, HTTPException
from app.api.v1.schemas.posts import (
    PostCreateRequest,
    PostGetResponse,
    PostCreateResponse,
    PostUpdateRequest,
    PostUpdateResponse,
    PostDeleteResponse,
)

log = logging.getLogger(__name__)

router = APIRouter(prefix="/posts-configuration", tags=["Posts configuration"])

post_raw: list = [
    {
        "title": "Introduction to Python",
        "content": "Python is a versatile programming language widely used for web development, data analysis, and automation.",
    },
    {
        "title": "FastAPI Basics",
        "content": "FastAPI is a modern, fast web framework for building APIs with Python using type hints.",
    },
    {
        "title": "Data Engineering",
        "content": "Data engineering focuses on building pipelines to collect, transform, and store data for analysis.",
    },
    {
        "title": "Unit Testing",
        "content": "Unit testing ensures that individual components of your code work as expected.",
    },
    {
        "title": "CI/CD Pipelines",
        "content": "CI/CD automates testing and deployment processes to improve software delivery speed and reliability.",
    },
    {
        "title": "Docker Overview",
        "content": "Docker allows developers to package applications and dependencies into containers for consistent environments.",
    },
    {
        "title": "RESTful APIs",
        "content": "RESTful APIs follow a set of conventions for building scalable and maintainable web services.",
    },
    {
        "title": "Async Programming",
        "content": "Async programming enables concurrent execution of tasks, improving performance in I/O-bound applications.",
    },
    {
        "title": "Database Indexing",
        "content": "Indexes improve query performance by allowing faster data retrieval from databases.",
    },
    {
        "title": "Logging Best Practices",
        "content": "Proper logging helps in debugging, monitoring, and maintaining applications in production.",
    },
]
post_data: dict = {i: item for i, item in enumerate(post_raw)}


@router.get("/posts")
def get_all_posts(limit: int) -> list:
    posts = list(post_data.values())
    if limit:
        return posts[:limit]
    return posts


@router.get("/posts/{id}")
def get_post(id: int) -> PostGetResponse:
    if id not in post_data:
        raise HTTPException(status_code=404, detail="Post not found.")

    post = post_data[id]
    return PostGetResponse(title=post["title"], content=post["content"])


@router.post("/posts")
def create_post(post: PostCreateRequest) -> PostCreateResponse:
    new_post = {"title": post.title, "content": post.content}
    post_data[max(post_data.keys()) + 1] = new_post
    wc = len(new_post["content"].split())
    return PostCreateResponse(title=post.title, content=post.content, word_count=wc)


@router.put("/posts/{id}")
def update_post(id: int, body: PostUpdateRequest) -> PostUpdateResponse:
    if id not in post_data:
        raise HTTPException(status_code=404, detail="Post not found.")
    post = post_data[id]

    old_title = post["title"]
    old_content = post["content"]
    post["title"] = body.title
    post["content"] = body.content

    return PostUpdateResponse(
        old_title=old_title,
        old_content=old_content,
        new_title=post["title"],
        new_content=post["content"],
    )


@router.delete("/posts/{id}")
def delete_post(id: int) -> PostDeleteResponse:
    if id not in post_data:
        raise HTTPException(status_code=404, detail="Post not found.")
    post = post_data[id]
    title = post["title"]
    content = post["content"]
    post_data.pop(id)
    return PostDeleteResponse(id=id, title=title, content=content)
