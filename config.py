"""
Nombre del proyecto: Proyecto Backend
Versión: 1.0
Autor: Valadez Barajas Jose Angel
"""
import os

"""
    Clase de configuración para la aplicación.
"""
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:pass@127.0.0.1:3306/pythonbd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  
    SECRET_KEY = 'clave'
    DEBUG = True  
config = {
    'development': Config,
    'production': Config,
    'testing': Config,
}
flask_env = os.getenv('FLASK_ENV', 'development')
config_class = config[flask_env]
