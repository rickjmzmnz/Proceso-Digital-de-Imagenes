Alumno: Jiménez Méndez Ricardo
No. de cuenta: 311085943

El programa fue escrito con el lenguaje de programación Python en su versión 2.7
Se probo en Ubuntu 16.04
A continuación se indica todo lo que se necesita instalar para poder ejecutar el programa:

°Instalar Python
sudo apt-get install python

°Instalar los paquetes para poder buscar archivos
sudo apt-get install python-tk

°Instalar los paquetes para poder facilitar el uso de paquetes en Python
sudo apt-get install python-setuptools

°Instalar pip que es un sistema de manejo de paquetes escritos en Python
sudo apt-get install python-pip

°Actualizar pip
sudo pip install --upgrade pip

°Instalar los paquetes para el proceso de imagenes
sudo pip install pillow

°Instalar los paquetes para el manejo de matrices
sudo pip install numpy

Con esto instalado podemos ejecutar el programa con el comando
python Principal.py

Se abrirá una ventana con varias opciones en la parte superior
En la parte de imagen tendremos la opción de abrir una imagen
Al seleccionar una imagen, se colocará en la parte izquierda y derecha
La izquierda se mantendrá sin cambios al aplicar el filtro y la segunda es la que cambiará al aplicar los filtros
Tenemos la opción de guardar la imagen con el filtro aplicado en formato jpg o png

En la pestaña de filtros se puede seleccionar el filtro que se quiere aplicar
Y en la pestaña de convolucion se puede seleccionar todo filtro que use esa tećnica
