from functools import wraps
from flask import request, jsonify
from datetime import datetime, timedelta
from app.models import Usuario
from config import Config
import jwt 

SECRET_KEY = Config.SECRET_KEY

def generate_token(username, rol):
    payload = {
        'username': username,
        'rol': rol,
        'exp': datetime.utcnow() + timedelta(days=1)  
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token




