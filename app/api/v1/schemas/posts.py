from pydantic import BaseModel


class PostGetResponse(BaseModel):
    title: str
    content: str


class PostCreateRequest(BaseModel):
    title: str
    content: str


class PostCreateResponse(BaseModel):
    title: str
    content: str
    word_count: int


class PostUpdateRequest(BaseModel):
    title: str
    content: str


class PostUpdateResponse(BaseModel):
    old_title: str
    old_content: str
    new_title: str
    new_content: str


class PostDeleteResponse(BaseModel):
    id: int
    title: str
    content: str
