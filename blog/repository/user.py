from sqlalchemy.orm import Session

from .. import models, schemas, hashing


def create(request: schemas.User, db: Session):
    new_user = models.User(name=request.Name, email=request.Email, password=hashing.Hash.bcrypt(request.Password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
