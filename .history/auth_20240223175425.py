from passlib.context import CryptContext
from fastapi import HTTPException, Depends
from datetime import datetime, timedelta
import jwt
from jwt import PyJWTError
from fastapi.security import OAuth2PasswordBearer
from . import models

# Secret key for encoding and decoding JWT tokens
SECRET_KEY = "your-secret-key"
# Algorithm used for encoding and decoding JWT tokens
ALGORITHM = "HS256"
# Token expiration time (in minutes)
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    """
    Verify the plain password against the hashed password.
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """
    Generate a hashed version of the password.
    """
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Create a new JWT access token.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Get the current user based on the provided JWT token.
    """
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except PyJWTError:
        raise credentials_exception
    user = models.User.query.filter(models.User.username == username).first()
    if user is None:
        raise credentials_exception
    return user

async def get_user_by_username(username: str, db: Session):
    """
    Retrieve a user by username from the database.
    """
    return db.query(models.User).filter(models.User.username == username).first()

async def authenticate_user(username: str, password: str, db: Session):
    """
    Authenticate a user based on username and password.
    """
    user = await get_user_by_username(username, db)
    if not user or not verify_password(password, user.password):
        return None
    return user