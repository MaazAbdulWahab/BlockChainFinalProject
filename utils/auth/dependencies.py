from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from utils.auth.jwt import decode_access_token
from utils.user.fakedb import getuser

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="authentication/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = decode_access_token(token)

    user = getuser(payload.get("id"))
    if user is None:
        raise credentials_exception
    return user


def require_role(required_role: str):
    def role_checker(current_user=Depends(get_current_user)):
        print("CURRENT USER COMING TO BE")

        print(current_user)
        if current_user.get("role") != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have access to this resource",
            )
        return current_user

    return role_checker
