import jwt 
from fastapi import HTTPException,status
import models, schemas

from fastapi.responses import JSONResponse
JWT_SECRET="PASSWORD"
JWT_ALGORITHM="HS256"

def signJWT(userID:int,role:str):
    payload={
        "userID":userID,
        "role":role
    }
    token=jwt.encode(payload,JWT_SECRET,algorithm=JWT_ALGORITHM)
    return {"token":token,"payload":payload}

def signJWT_client(clientID:int):
    signed=signJWT(clientID,"client")
    response = JSONResponse(content={"success":"client logged in","UserData":signed["payload"],'jwt':signed})
    response.set_cookie(key="jwt", value=signed["token"])
    return response


def decodeJWT(token:str):
    try:
        print("jwt="+str(token))
        user_data=jwt.decode(token,JWT_SECRET,algorithms=JWT_ALGORITHM)
        print(user_data)
        return user_data
    except jwt.exceptions.InvalidSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="JWT invalid"
        )

