from pydantic import BaseModel


class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True


class Blog(BaseModel):
    title: str
    body: str


class ShowBlog(Blog):
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class User(BaseModel):
    Name: str
    Email: str
    Password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
