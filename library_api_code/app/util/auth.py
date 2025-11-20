from datetime import datetime, timedelta, timezone
from jose import jwt
import jose
from functools import wraps
from flask import request, jsonify

SECRET_KEY = 'super secret secrets'

def encode_token(user_id, role="user"):
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(days=0, hours=1), #Set an expiration date of 1 hour from now
        'iat': datetime.now(timezone.utc),
        'sub': str(user_id), #VERY IMPORTANT, SET YOUR USER ID TO A STR
        'role': role #You will probably not have role unless you add it to your models
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def token_required(f): #f stands for the function that is getting wrapped
    @wraps(f)
    def decoration(*args, **kwargs): #The function that runs before the functiuon that we're wrapping

        token = None

        if 'Authorization' in request.headers:
            # Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjM1MTgwMTQsImlhdCI6MTc2MzUxNDQxNCwic3ViIjoiMSIsInJvbGUiOiJBZG1pbiJ9.2gEKkaU_LEQAxEPbj5734khp4k6jKMgJQsayui70iPw
            token = request.headers['Authorization'].split()[1]
        
        if not token:
            return jsonify({"error": "token missing from authorization headers"}), 401
        
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            print(data)
            request.logged_in_user_id = data['sub'] #Adding the user_id from the token to the request
        except jose.exceptions.ExpiredSignatureError:
            return jsonify({'message':'token is expired'}), 403
        except jose.exceptions.JWTError:
            return jsonify({'message':'invalid token'}), 401
        
        return f(*args, **kwargs)
    
    return decoration