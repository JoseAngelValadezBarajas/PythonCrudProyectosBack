from app import db

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
