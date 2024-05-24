from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from utils.user.user_utils import finduser, create_contractor
from utils.auth.jwt import create_access_token
from typings import PasswordChangeRequest, SignUpContractor
import uuid
from passlib.hash import pbkdf2_sha256


authentication_router = APIRouter(
    prefix="/authentication",
    tags=["authentication"],
)


@authentication_router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    foundUser = finduser(username, password)
    if not foundUser:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not validate credentials",
        )
    access_token = create_access_token({"id": foundUser["id"]})
    return {"access_token": access_token}


@authentication_router.post("/signup-contractor")
async def signup(signup: SignUpContractor):
    id = str(uuid.uuid4())
    signup.password = pbkdf2_sha256.hash(signup.password)
    contractor = create_contractor(id, signup.model_dump())

    return {"id": id, "contractor": contractor}
