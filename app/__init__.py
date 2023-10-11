"""
Nombre del proyecto: Proyecto Backend
Versión: 1.0
Autor: Valadez Barajas Jose Angel
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_cors import CORS
from flask import request, jsonify, Blueprint, make_response

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SECRET_KEY'] = Config.SECRET_KEY

db = SQLAlchemy(app)
from app.routes import proyectos_bp  
from app.routes import auth_bp
app.register_blueprint(proyectos_bp)
app.register_blueprint(auth_bp)
"""
    Maneja las solicitudes OPTIONS para la raíz del proyecto.
    :return: Respuesta con encabezados CORS configurados.
    :rtype: make_response
"""
@app.route('/', methods=['OPTIONS'])
def handle_options():
    response = make_response()
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response, 200

"""
    Maneja las solicitudes después de su procesamiento.
    :param response: Respuesta a la solicitud.
    :type response: make_response
    :return: Respuesta con encabezados CORS configurados.
    :rtype: make_response
"""
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response
def create_app():
    return app
