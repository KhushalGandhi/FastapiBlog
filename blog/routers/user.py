from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..repository import user

from .. import schemas, database, models, hashing

router = APIRouter(
    prefix="/user",
    tags=['users']

)


@router.post('/')
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)
