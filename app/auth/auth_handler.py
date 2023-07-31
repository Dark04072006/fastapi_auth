import time
from typing import Dict

import jwt

from core.settings import JWT_ALGORITHM, JWT_SECRET


def token_response(token: str):
    return {
        "access_token": token
    }

# function used for signing the JWT string
def signJWT(identity: str) -> Dict[str, str]:
    payload = {
        "identity": identity,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}

def verify_jwt(jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid