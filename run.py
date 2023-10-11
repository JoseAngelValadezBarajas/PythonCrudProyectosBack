"""
Nombre del proyecto: Proyecto Backend
Versión: 1.0
Autor: Valadez Barajas Jose Angel
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
