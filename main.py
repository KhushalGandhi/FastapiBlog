# This is a sample Python script.

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

app = FastAPI()


@app.get("/")
def index():
    return {'data': {'name': 'Sarthak'}}
    # Use a breakpoint in the code line below to debug your script.


@app.get('/about/{id}')
def about(blogid):
    return {'id': blogid}


@app.get('/about?{limit}')
def about(limit):
    return {'data': f'{limit} blogs from the list'}


class Blog(BaseModel):
    Title: str
    body: str
    published_at: Optional[bool]


@app.post('/blogs')
def blogs(request: Blog):
    return request
