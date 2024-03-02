from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..repository import blog

from .. import schemas, database, models,oauth2

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)


@router.get('/')
def allblogs(db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/')
def blogs(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def getblogid(id, db: Session = Depends(database.get_db)):
    return blog.getId(id, db)


@router.delete('/{id}')
def deleteblogid(id, db: Session = Depends(database.get_db)):
    return blog.delete(id, db)


@router.put('/{id}')
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update(id, request, db)
