"""
Autor: Valadez Barajas Jose Angel
Versión: 1.0
"""
from flask_sqlalchemy import SQLAlchemy
from config import Config
db = SQLAlchemy()
"""
    Inicializa la base de datos de la aplicación.
    :param app: La aplicación Flask.
    :type app: Flask
"""
def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] =Config.SQLALCHEMY_DATABASE_URI
    db.init_app(app)


