from fastapi import APIRouter, HTTPException, status
from database import users_collection
from models import UserCreate, UserLogin
from auth import hash_password, verify_password, create_access_token

router = APIRouter()


# -------- REGISTER USER --------
@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate):
    existing_user = users_collection.find_one({"email": user.email})

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    hashed_password = hash_password(user.password)

    new_user = {
        "name": user.name,
        "email": user.email,
        "password": hashed_password
    }

    users_collection.insert_one(new_user)

    return {"message": "User registered successfully"}


# -------- LOGIN USER --------
@router.post("/login")
def login_user(user: UserLogin):
    db_user = users_collection.find_one({"email": user.email})

    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    token = create_access_token({"sub": db_user["email"]})

    return {
        "access_token": token,
        "token_type": "bearer"
    }
