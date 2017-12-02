import os
import types
import math
from PIL import Image
import PIL.Image

"""
Recibe la ruta de las imagenes y la imagen a buscar
Busca por todas las carpetas y se regresa la imagen solicitada
"""
def buscaImagen(path,imagen):
    lista = os.listdir(path)
    for i in lista:   
        l = path + "/" + str(i)
        imagesL = [f for f in os.listdir(l) if os.path.splitext(f)[-1] == '.JPG' or os.path.splitext(f)[-1] == '.jpg']
        for image in imagesL:
            if(imagen == image):
                nueva = Image.open(l + "/" + imagen)
                return nueva

"""
Escribe en un archivo el nombre de la imagen procesada y su promedio de rgb
"""
def guardaImagenes(path,nombre):
    lista = os.listdir(path)
    archivo = open(nombre + ".txt","w")
    for i in lista:   
        l = path + "/" + str(i)
        imagesL = [f for f in os.listdir(l) if os.path.splitext(f)[-1] == '.JPG' or os.path.splitext(f)[-1] == '.jpg']
        try:
            for image in imagesL:
                imagen = Image.open(l + "/" + image)
                elemento = calculaPromedio(imagen)
                archivo.write(image + " " + str(elemento[0]) + " " + str(elemento[1]) + " " + str(elemento[2]) + " " + "\n")
        except IOError:
            pass
    archivo.close()
            
"""
Calcula la distancia euclidiana entre dos puntos
"""
def distanciaEuclidiana(r1,g1,b1,r2,g2,b2):
    rc = (r2-r1)**2
    gc = (g2-g1)**2
    bc = (b2-b1)**2
    dis = math.sqrt(rc+gc+bc)
    return dis

"""
Pasa la informacion del archivo imagenes.txt a una lista
"""
def sacaInfo(archivo):
    lista = []
    f = open(archivo + ".txt","r")
    imagenes = f.readlines()
    for line in imagenes:
        elemento = line.split(" ")
        lista.append(elemento)
    return lista

"""
Elige la mejor imagen a colocar en el mosaico
"""
def eligeImagen(lista,r,g,b):
    n = None
    imagen = None
    for i in lista:
        relem = int(i[1])
        gelem = int(i[2])
        belem = int(i[3])
        dis = distanciaEuclidiana(relem,gelem,belem,r,g,b)
        if(n == None):
            n = dis
            imagen = i[0]
        if(dis < n):
            imagen = i[0]
    return imagen
        

"""
Calcula el valor promedio del rgb de la imagen
"""
def calculaPromedio(imagen):
    ancho = imagen.size[0]
    alto = imagen.size[1]
    rgb = imagen.convert('RGB')
    rprom = 0
    gprom = 0
    bprom = 0
    promedio = 0
    for i in range(ancho):
        for j in range(alto):
            r,g,b = rgb.getpixel((i,j))
            rprom += r
            gprom += g
            bprom += b
            promedio += 1
    promRojo = rprom/promedio
    promVerde = gprom/promedio
    promAzul = bprom/promedio
    return (promRojo,promVerde,promAzul)

"""
Saca los valores promedios del mosaico que calcula
Obtiene la representacion hexadecimal de esos valores
y busca una imagen con esos valores para colocarla en el mosaico
"""
def filtroFotoMosaico(imagen,aplica,carpeta,mosX,mosY,archivo):
    lista = sacaInfo(archivo)
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
            cadena = eligeImagen(lista,promRojo,promVerde,promAzul)
            img = buscaImagen(carpeta,cadena)
            img = img.resize(size)
            aplica.paste(img,(posX,posY))
            posY += mosY
        posX += mosX
        posY = 0
    return aplica
