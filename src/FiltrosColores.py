from PIL import ImageTk, Image
from random import randint

"""
Filtro mica roja
Recorremos cada pixel de la imagen y ponemos en 0 cada entrada verde y azul
Solo dejamos el valor del rojo
"""
def filtroRojo(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()    
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            pixels[i,j] = (r,0,0)
    return aplica

""" 
Filtro mica azul
Recorremos cada pixel de la imagen y ponemos en 0 cada entrada verde y rojo
Solo dejamos el valor del azul
"""    
def filtroAzul(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()    
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            pixels[i,j] = (0,0,b)
    return aplica

""" 
Filtro mica verde
Recorremos cada pixel de la imagen y ponemos en 0 cada entrada rojo y azul
Solo dejamos el valor del verde
"""
def filtroVerde(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()        
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            pixels[i,j] = (0,g,0)
    return aplica

"""
Filtro Azar
Coloca valores aleatorios entre 0 y 255 a cada entrada del rgb de los pixeles
"""
def filtroAzar(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()  
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            pixels[i,j] = (r,g,b)
    return aplica
