import os
import tkFileDialog
import types
from PIL import Image

"""
Recibe la ruta de las imagenes y la imagen a buscar
Busca por todas las carpetas y se regresa la imagen solicitada
"""
def buscaImagen(path,imagen):
    lista = os.listdir(path)
    for i in lista:   
        l = path + "/" + str(i)
        imagesL = [f for f in os.listdir(l) if os.path.splitext(f)[-1] == '.JPG']
        for image in imagesL:
            if(imagen == image):
                nueva = Image.open(l + "/" + imagen)
                return nueva

"""
Dados tres valores en rgb, se regresa su representacion en hexadecimal
"""
def convierteHex(r,g,b):
    sr = hex(r)
    sr = sr[2:]
    sg = hex(g)
    sg = sg[2:]
    sb = hex(b)
    sb = sb[2:]
    s = sr + sg + sb
    s = s.upper()
    cadena = "P0" + s + ".JPG"
    return cadena

"""
Saca los valores promedios del mosaico que calcula
Obtiene la representacion hexadecimal de esos valores
y busca una imagen con esos valores para colocarla en el mosaico
"""
def filtroFotoMosaico(imagen,aplica,carpeta,mosX,mosY):
    size = mosX,mosY
    posX = 0
    posY = 0
    recorreX = 0
    recorreY = 0
    rprom = 0
    gprom = 0
    bprom = 0
    promedio = 0
    ancho = imagen.size[0]
    alto = imagen.size[1]
    rgb = imagen.convert('RGB')
    pixels = aplica.load()
    for i in range(0,ancho,mosX):
        recorreX = i + mosX
        for j in range(0,alto,mosY):
            recorreY = j + mosY
            for k in range(i,recorreX):
                if (k >= ancho):
                    break
                for l in range(j,recorreY):
                    if (l >= alto):
                        break
                    r,g,b = rgb.getpixel((k,l))
                    rprom += r
                    gprom += g
                    bprom += b
                    promedio += 1
            promRojo = (rprom/promedio)
            promVerde = (gprom/promedio)
            promAzul = (bprom/promedio)
            rprom = 0
            gprom = 0
            bprom = 0
            promedio = 0
            cadena = convierteHex(promRojo,promVerde,promAzul)
            img = buscaImagen(carpeta,cadena)
            img = img.resize(size)
            aplica.paste(img,(posX,posY))
            posY += mosY
        posX += mosX
        posY = 0
    return aplica

