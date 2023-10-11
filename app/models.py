"""
Autor: Valadez Barajas Jose Angel
Versión: 1.0
"""
from app import db

"""
    Clase que representa la entidad Proyecto en la base de datos.
    :param id: Identificador único del proyecto.
    :type id: int
    :param nombre: Nombre del proyecto.
    :type nombre: str
    :param projectManager: Nombre del gerente del proyecto.
    :type projectManager: str
    :param descripcion: Descripción del proyecto.
    :type descripcion: str
    :param desarrolladores: Lista de desarrolladores del proyecto.
    :type desarrolladores: str
"""
class Proyecto(db.Model):
    __tablename__ = 'proyectos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    projectManager = db.Column(db.String(255))
    descripcion = db.Column(db.Text)
    desarrolladores = db.Column(db.Text)

    def __init__(self, nombre, projectManager, descripcion, desarrolladores):
        self.nombre = nombre
        self.projectManager = projectManager
        self.descripcion = descripcion
        self.desarrolladores = desarrolladores
        
"""
    Clase que representa la entidad Usuario en la base de datos.
    :param id: Identificador único del usuario.
    :type id: int
    :param username: Nombre de usuario.
    :type username: str
    :param password: Contraseña del usuario.
    :type password: str
    :param rol: Rol del usuario.
    :type rol: str
"""
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(255), nullable=False)

    def __init__(self, username, password, rol):
        self.username = username
        self.password = password
        self.rol = rol
