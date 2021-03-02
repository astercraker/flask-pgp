# Crear entorno virtual
Para empezar con el desarrolo del projecto primero tenemos que crear nuestro entorno virtual.

    python -m venv venv
En el ejemplo anterior usamos la convencion de nombrar venv al entorno virtual pero puede ser el que decida.
Siempre que trabaje con el proyecto debe activar el entorno virtual, asi como la instalacion de paquetes.

    venv/Scripts/activate

# Instalación de paquetes

La instalacion de paquetes necesarios se pueden hacer mediante el archivo requirements.txt que se encuentra dentro del proyecto de la siguiente manera.

    pip install -r requirements.txt
De igual manera debe crearse el archivo si instala un paquete, debe usar el comando

    pip freeze > requirements.txt

