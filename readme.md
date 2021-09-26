# Requerimientos

- Python3.8   https://www.python.org/downloads/

# Paso previo
-  python3 -m venv entornoAgil https://docs.python.org/es/3/tutorial/venv.html
-  cd entornoAgil 
-  git clone https://github.com/enzostefani507/agilidad/

# Instrucciones
* cd entornoAgil
* source bin/activate
* cd Agilidad
* pip3 install -r requirements.txt
* python3 manage.py makemigrations
* python3 manage.py migrate --run-sync
* python3 manage.py runserver

# Propone cambios
Los commit preferentemente con el siguiente formato:
"nombre_app_modificada | funcion [fix:]"

Si haces cambios agregando librerias recorda actualizar el registro haciendo:
pip3 freeze > requirements.txt

# Problemas comunes
- Creacion del super usuario
    Para las pruebas el super usuario se crea por consola con el comando
        python3 manage.py createsuperuser

- Estetica rota en local
    Debug (en settings) en el servidor local tiene que estar en False, para produccion se instala una libreria que se encarga.
