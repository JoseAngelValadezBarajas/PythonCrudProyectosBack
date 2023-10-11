# PythonCrudProyectosBack
Favor de revisar los documentos .docx presentes en este repositorio, son las guias detalladas de instalacion, configuracion y manejo de la web.<br>

La estructura del proyecto es la siguiente:<br>
proyecto-flask/<br>
│<br>
├── app/<br>
│   ├── __init__.py<br>
│   ├── models.py<br>
│   ├── auth.py<br>
│   ├── routes.py<br>
│<br>
├── config.py<br>
├── manage.py<br>
├── requirements.txt<br>
├── run.py<br>

Pasos para trabajar con el proyecto.....<br>
1.-Clona el repositorio de Flask en tu máquina local:<br>
-git clone <https://github.com/JoseAngelValadezBarajas/PythonCrudProyectosBack.git><br>
2.-Instala las dependencias del proyecto Flask desde el archivo requirements.txt:<br>
-pip install -r requirements.txt<br>
3.-En el archivo config.py se encuentra un string de conexion de ejemplo, remplaza por la que tu vayas a requerir<br>
-SQLALCHEMY_DATABASE_URI = 'Tu String Va Aqui, el ejemplo esta dentro del codigo'<br>
4.-Ejecuta la aplicación<br>
-python run.py<br>

Pasos para la base de datos....<br>
1.-Crea tu base de datos de preferencia con el nombre: `pythonbd`<br>
-CREATE DATABASE pythonbd;<br>
2.-Ejecuta las siguientes querrys en tu base de datos ya creada<br>
CREATE TABLE usuarios (<br>
    id SERIAL PRIMARY KEY,<br>
    username VARCHAR(255) NOT NULL,<br>
    password VARCHAR(255) NOT NULL,<br>
    rol VARCHAR(255)<br>
);<br>
CREATE TABLE proyectos (<br>
    id SERIAL PRIMARY KEY,<br>
    nombre VARCHAR(255) NOT NULL,<br>
    projectManager VARCHAR(255),<br>
    descripcion TEXT,<br>
    desarrolladores TEXT<br>
);<br>
3.-Pobla la base de datos con los siguientes querrys<br>
INSERT INTO usuarios (username, password, rol) VALUES ('admin', 'pass', 'admin');<br>
INSERT INTO proyectos (nombre, projectManager, descripcion, desarrolladores) VALUES ('Proyecto 1', 'PM 1', 'Descripción del Proyecto 1', 'Desarrollador 1, Desarrollador 2');<br>
INSERT INTO proyectos (nombre, projectManager, descripcion, desarrolladores) VALUES ('Proyecto 2', 'PM 2', 'Descripción del Proyecto 2', 'Desarrollador 3, Desarrollador 4');<br>
INSERT INTO proyectos (nombre, projectManager, descripcion, desarrolladores) VALUES ('Proyecto 3', 'PM 3', 'Descripción del Proyecto 3', 'Desarrollador 5, Desarrollador 6');<br>
