Instrucciones para utilizar el proyecto (espero...)

Dentro de la carpeta descargada y despues de haberla abierto en VS Code (asegurandonos que estamos en la ruta correcta)

Realizamos lo siguiente:

python -m venv venv

Despues: 

venv\Scripts\activate

Instalamos las dependencias:
(django para el framework utilizado, modulos, etc.. y pillow es para las imagenes)
pip install Django pillow 

Ahora procedemos a crear la base de datos:

python manage.py migrate 

python manage.py makemigrations (si no recuerdo mal este es para cuando se añaden las tablas proceder a realizar los cambios)

Ahora para crear el usuario en este caso un superusuario (admin):

python manage.py createsuperuser

Ocupamos de nombre: ES02
Email lo dejamos vacio
Contraseña: pbe-es-02 

Por que no subimos la base de datos?

Si no me equivoco en la rubrica salia algo de subir archivos, pero tambien creo que es mas eficiente para el profesor o puede darle mas libertad al momento de testear una base de datos completamente limpia
por ejemplo asi no se sube lo que yo hice, imagenes, juegos ya creados (en este caso de eso trata mi tienda) y simplemente le da mas "juego" al profesor

Una vez hecho todo esto realizamos el inicio del servidor con:

python manage.py runserver 
