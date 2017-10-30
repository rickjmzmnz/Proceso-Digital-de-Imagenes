import os
import math
from PIL import ImageTk, Image
import PIL.Image
from TonosGris import *

def semitonosCirculos(imagen,aplica,mosX,mosY):
    gris = filtroGris1(imagen,aplica)
    size = mosX,mosY
    posX = 0
    posY = 0
    recorreX = 0
    recorreY = 0
    grisProm = 0
    promedio = 0
    ancho = gris.size[0]
    alto = gris.size[1]
    rgb = gris.convert('RGB')
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
                    grisProm += r
                    promedio += 1
            promRec = (grisProm/promedio)
            grisProm = 0
            promedio = 0
            if(promRec >= 0 and promRec < 25):
                img = PIL.Image.open('circulos/circulo1.jpg')
                img = img.resize(size)
                aplica.paste(img,(posX,posY))
            elif(promRec >= 25 and promRec < 50):
                img = PIL.Image.open('circulos/circulo2.jpg')
                img = img.resize(size)
                aplica.paste(img,(posX,posY))
            elif(promRec >= 50 and promRec < 75):
                img = PIL.Image.open('circulos/circulo3.jpg')
                img = img.resize(size)
                aplica.paste(img,(posX,posY))
            elif(promRec >= 75 and promRec < 100):
                img = PIL.Image.open('circulos/circulo4.jpg')
                img = img.resize(size)
                aplica.paste(img,(posX,posY))
            elif(promRec >= 100 and promRec < 125):
                img = PIL.Image.open('circulos/circulo5.jpg')
                img = img.resize(size)
                aplica.paste(img,(posX,posY))
            elif(promRec >= 125 and promRec < 150):
                img = PIL.Image.open('circulos/circulo6.jpg')
                img = img.resize(size)
                aplica.paste(img,(posX,posY))
            elif(promRec >= 150 and promRec < 175):
                img = PIL.Image.open('circulos/circulo7.jpg')
                img = img.resize(size)
                aplica.paste(img,(posX,posY))
            elif(promRec >= 175 and promRec < 200):
                img = PIL.Image.open('circulos/circulo8.jpg')
                img = img.resize(size)
                aplica.paste(img,(posX,posY))
            elif(promRec >= 200 and promRec < 225):
                img = PIL.Image.open('circulos/circulo9.jpg')
                img = img.resize(size)
                aplica.paste(img,(posX,posY))
            elif(promRec >= 225 and promRec < 255):
                img = PIL.Image.open('circulos/blanco.jpg')
                img = img.resize(size)
                aplica.paste(img,(posX,posY))
            posY += mosY
        posX += mosX
        posY = 0
    return aplica
