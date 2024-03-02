from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette import status
import blog.token as auth

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(tokens: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return auth.verify_token(tokens,credentials_exception)


