from PIL import ImageTk, Image
from TonosGris import *

"""
Tomamos la imagen y la pasamos a tono de gris
Hacemos la suma del rojo,verde y azul, el resultado lo divimos entre 3
Si resutado >= 128 ponemos cada entrada igual a 255
Si resultado < 128 ponemos cada entrada igual a 0
"""
def filtroAltoContraste(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            prom = (r+g+b)/3
            if prom >= 128:
                prom  = 255
            elif prom < 128:
                prom = 0
            pixels[i,j] = (prom,prom,prom)
    return aplica


"""
Tomamos la imagen y la pasamos a tono de gris
Hacemos la suma del rojo,verde y azul, el resultado lo divimos entre 3
Si resutado < 128 ponemos cada entrada igual a 255
Si resultado >= 128 ponemos cada entrada igual a 0
"""
def filtroInverso(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            prom = (r+g+b)/3
            if prom < 128:
                prom  = 255
            elif prom >= 128:
                prom = 0
            pixels[i,j] = (prom,prom,prom)
    return aplica
