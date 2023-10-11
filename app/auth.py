"""
Autor: Valadez Barajas Jose Angel
Versión: 1.0
"""
from functools import wraps
from flask import request, jsonify
from datetime import datetime, timedelta
from app.models import Usuario
from config import Config
import jwt 

SECRET_KEY = Config.SECRET_KEY
"""
    Genera un token JWT con información de usuario y rol.
    :param username: Nombre de usuario.
    :type username: str
    :param rol: Rol del usuario.
    :type rol: str
    :return: Token JWT generado.
    :rtype: str
"""
def generate_token(username, rol):
    payload = {
        'username': username,
        'rol': rol,
        'exp': datetime.utcnow() + timedelta(days=1)  
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token




