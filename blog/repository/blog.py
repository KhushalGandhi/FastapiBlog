from fastapi import HTTPException
from sqlalchemy import false
from sqlalchemy.orm import Session
from starlette import status

from .. import models, schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def getId(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found", )

    return blog


def delete(id, db: Session):
    db.query(models.Blog).filter(models.Blog.id == id).first().delete(synchronize_session=false)
    db.commit()
    return 'done'


def update(id, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.update(request.dict())
    db.commit()
    return 'update'
