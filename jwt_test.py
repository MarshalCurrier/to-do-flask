import jwt
import datetime

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyODIzMTU1NiwianRpIjoiZjE0M2Q5MTQtNmFhNS00MmM5LWFhNWQtNDhkN2UwY2Q1ZDEwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRlc3QiLCJuYmYiOjE3MjgyMzE1NTYsImNzcmYiOiJkNDVkMDg3OS00NzczLTQwYTktOTEzYS1kZmM1MDlhMTRlNGUiLCJleHAiOjE3MjgyMzI0NTYsInJvbGUiOiJBZG1pbiIsImFjY291bnRfc3RhdHVzIjoiUGVuZGluZyJ9.Q3K8ThU8ThsB8OXQTej8ho3-jfRGshE-6vHB2SKvBBo'

secret = 'some super secret key'


def is_jwt_expired(token, secret_key, algorithm='HS256'):
    try:
        jwt.decode(token, secret_key, algorithms=[algorithm])
        return False  # Token is valid
    except jwt.ExpiredSignatureError:
        return True  # Token has expired
    except jwt.InvalidTokenError:
        return True  # Token is invalid for other reasons

# Example usage:
if is_jwt_expired(token, secret):
    print("Token has expired")
else:
    print("Token is valid")
    print(f"Toekn expires in: {datetime.datetime.fromtimestamp(jwt.decode(token, secret, algorithms='HS256')['exp'])}")