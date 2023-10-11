"""
Autor: Valadez Barajas Jose Angel
Versión: 1.0
"""
from flask import Flask
from flask_cors import CORS
from flask import request, jsonify, Blueprint, make_response
from functools import wraps
from jwt import decode, exceptions
from app import db
from app.models import Proyecto
from app.models import Usuario
from app.auth import generate_token
from config import Config

#CONFIGURACION DE BLUEPRINT
proyectos_bp = Blueprint('Proyecto', __name__)
auth_bp = Blueprint('Usuario', __name__)

#CONFIGURACION SE SECRET_KEY
SECRET_KEY = Config.SECRET_KEY

"""
    Función decoradora que requiere autenticación del administrador.
    :param f: Función a decorar.
    :type f: function
    :returns: Función decorada.
    :rtype: function
"""
def admin_required_with_cookie(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('auth_token')
        if token_valid(token):
            return f(*args, **kwargs)
        else:
            return jsonify({"message": "No eres admin"}, 401)  
    return decorated_function

"""
    Verifica si el token es válido.
    :param token: Token a verificar.
    :type token: str
    :returns: True si el token es válido, False de lo contrario.
    :rtype: bool
"""
def token_valid(token):
    try:
        payload = decode(token, SECRET_KEY, algorithms=['HS256'])
        if 'rol' in payload and payload['rol'] == 'admin':
            return True
        else:
            return jsonify({"message": "No eres admin"}, 401)
    except exceptions.ExpiredSignatureError:
        return jsonify({"message": "Relogea"}, 401)
    except exceptions.DecodeError:
        return jsonify({"message": "Error en el servidor"}, 403) 

#RUTAS DE LOGIN
"""
    Ruta para iniciar sesión.
    :returns: Mensaje de éxito o error.
    :rtype: str
"""
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True, silent=True)
    #data = request.json
    username = data.get('username')
    password = data.get('password')
    user = Usuario.query.filter_by(username=username, password=password).first()
    if user and user.rol == 'admin':
        token = generate_token(username, user.rol)
        response = make_response({"Token": "Inicio de sesión exitoso"})
        response_data = {"message": "Inicio de sesión exitoso", "token": token}
        response.set_cookie("auth_token", token, httponly=True, secure=True)
        return response_data
    else:
        return jsonify({"message": "Inicio de sesión fallido"})  
    


#RUTAS PARA CONSUMO DE API CON AUTH  
"""
    Ruta para obtener todos los proyectos (requiere autenticación).
    :returns: Lista de proyectos.
    :rtype: list
""" 
@proyectos_bp.route('/servicios/auth/proyectos', methods=['GET'])
@admin_required_with_cookie
def get_auth_proyectos():
    proyectos = Proyecto.query.all()
    proyectos_json = [{"id": proyecto.id,"nombre": proyecto.nombre, "projectManager": proyecto.projectManager, "descripcion": proyecto.descripcion, "desarrolladores": proyecto.desarrolladores} for proyecto in proyectos]
    return jsonify({"proyectos": proyectos_json})

"""
    Ruta para obtener un proyecto por su ID (requiere autenticación).
    :param id: ID del proyecto.
    :type id: int
    :returns: Detalles del proyecto.
    :rtype: dict
"""
@proyectos_bp.route('/servicios/auth/proyectos/<int:id>', methods=['GET'])
@admin_required_with_cookie
def get_proyecto(id):
    proyecto = Proyecto.query.get(id)
    if proyecto:
        proyecto_json = {"nombre": proyecto.nombre, "projectManager": proyecto.projectManager, "descripcion": proyecto.descripcion, "desarrolladores": proyecto.desarrolladores}
        return jsonify(proyecto_json)
    else:
        return jsonify({"message": "El proyecto no se encuentra en la base de datos"}, 404)

"""
    Ruta para agregar un nuevo proyecto (requiere autenticación).
    :returns: Mensaje de éxito o error.
    :rtype: str
"""
@proyectos_bp.route('/servicios/auth/proyectos', methods=['POST'])
@admin_required_with_cookie
def add_proyecto():
    data = request.json
    nuevo_proyecto = Proyecto(nombre=data["nombre"], projectManager=data["projectManager"], descripcion=data["descripcion"], desarrolladores=data["desarrolladores"])
    db.session.add(nuevo_proyecto)
    db.session.commit()
    return jsonify({"message": "Se ha agregado un nuevo proyecto"})

"""
    Ruta para actualizar un proyecto (requiere autenticación).
    :param id: ID del proyecto.
    :type id: int
    :returns: Mensaje de éxito o error.
    :rtype: str
"""
@proyectos_bp.route('/servicios/auth/proyectos/<int:id>', methods=['PUT'])
@admin_required_with_cookie
def update_proyecto(id):
    proyecto = Proyecto.query.get(id)
    if not proyecto:
        return jsonify({"message": "El proyecto no se encuentra en la base de datos"}, 404)
    data = request.json
    proyecto.nombre = data["nombre"]
    proyecto.projectManager = data["projectManager"]
    proyecto.descripcion = data["descripcion"]
    proyecto.desarrolladores = data["desarrolladores"]
    db.session.commit()
    return jsonify({"message": "Se ha actualizado el proyecto"})

"""
    Ruta para eliminar un proyecto (requiere autenticación).
    :param id: ID del proyecto.
    :type id: int
    :returns: Mensaje de éxito o error.
    :rtype: str
"""
@proyectos_bp.route('/servicios/auth/proyectos/<int:id>', methods=['DELETE'])
@admin_required_with_cookie
def delete_proyecto(id):
    proyecto = Proyecto.query.get(id)
    if not proyecto:
        return jsonify({"message": "El proyecto no se encuentra en la base de datos"}, 404)
    db.session.delete(proyecto)
    db.session.commit()
    return jsonify({"message": "El proyecto se ha eliminado"})



#RUTAS PARA CONSUMO DE API SIN AUTH

"""
    Ruta para obtener todos los proyectos (sin autenticación).
    :returns: Lista de proyectos.
    :rtype: list
"""  
@proyectos_bp.route('/servicios/open/proyectos', methods=['GET'])
def get_open_proyectos():
    proyectos = Proyecto.query.all()
    proyectos_json = [{"nombre": proyecto.nombre, "projectManager": proyecto.projectManager, "descripcion": proyecto.descripcion, "desarrolladores": proyecto.desarrolladores} for proyecto in proyectos]
    return jsonify({"proyectos": proyectos_json})





