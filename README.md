# flaskcrudwithreactjs

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
Clona el repositorio de Flask en tu máquina local:<br>
-git clone <URL_del_repositorio_de_Flask><br>
Instala las dependencias del proyecto Flask desde el archivo requirements.txt:<br>
-pip install -r requirements.txt<br>
En el archivo config.py se encuentra un string de conexion de ejemplo, remplaza por la que tu vayas a requerir<br>
-SQLALCHEMY_DATABASE_URI = 'Tu String Va Aqui, el ejemplo esta dentro del codigo'<br>
Ejecuta la aplicación<br>
-python run.py<br>
