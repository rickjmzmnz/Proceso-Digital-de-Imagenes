from PIL import ImageTk, Image
import numpy as np

global matriz
global factor
global bias

def blur1(imagen,aplica):

    matriz = np.matrix([[0.0,0.2,0.0]
                      , [0.2,0.2,0.2]
                      , [0.0,0.2,0.0]])
    factor = 1.0
    bias = 0.0
    img = convolucion(imagen,aplica,matriz,factor,bias)
    return img

def blur2(imagen,aplica):

    matriz = np.matrix([[0,0,1,0,0]
                      , [0,1,1,1,0]
                      , [1,1,1,1,1]
                      , [0,1,1,1,0]
                      , [0,0,1,0,0]])
    factor = 1.0/13.0
    bias = 0.0
    img = convolucion(imagen,aplica,matriz,factor,bias)
    return img

def motionBlur(imagen,aplica):

    matriz = np.matrix([[1,0,0,0,0,0,0,0,0]
                      , [0,1,0,0,0,0,0,0,0]
                      , [0,0,1,0,0,0,0,0,0]
                      , [0,0,0,1,0,0,0,0,0]
                      , [0,0,0,0,1,0,0,0,0]
                      , [0,0,0,0,0,1,0,0,0]
                      , [0,0,0,0,0,0,1,0,0]
                      , [0,0,0,0,0,0,0,1,0]
                      , [0,0,0,0,0,0,0,0,1]])
    factor = 1.0/9.0
    bias = 0.0
    img = convolucion(imagen,aplica,matriz,factor,bias)
    return img

def encuentraBordes1(imagen,aplica):

    matriz = np.matrix([[0,0,-1,0,0]
                      , [0,0,-1,0,0]
                      , [0,0, 2,0,0]
                      , [0,0, 0,0,0]
                      , [0,0, 0,0,0]])
    factor = 1.0
    bias = 0.0
    img = convolucion(imagen,aplica,matriz,factor,bias)
    return img

def encuentraBordes2(imagen,aplica):

    matriz = np.matrix([[0,0,-1,0,0]
                      , [0,0,-1,0,0]
                      , [0,0, 4,0,0]
                      , [0,0,-1,0,0]
                      , [0,0,-1,0,0]])
    factor = 1.0
    bias = 0.0
    img = convolucion(imagen,aplica,matriz,factor,bias)
    return img

def encuentraBordes3(imagen,aplica):

    matriz = np.matrix([[-1, 0,0, 0, 0]
                      , [ 0,-2,0, 0, 0]
                      , [ 0, 0,6, 0, 0]
                      , [ 0, 0,0,-2, 0]
                      , [ 0, 0,0, 0,-1]])
    factor = 1.0
    bias = 0.0
    img = convolucion(imagen,aplica,matriz,factor,bias)
    return img

def encuentraBordes4(imagen,aplica):

    matriz = np.matrix([[-1,-1,-1]
                      , [-1, 8,-1]
                      , [-1,-1,-1]])
    factor = 1.0
    bias = 0.0
    img = convolucion(imagen,aplica,matriz,factor,bias)
    return img

def sharpen1(imagen,aplica):

    matriz = np.matrix([[-1,-1,-1]
                      , [-1, 9,-1]
                      , [-1,-1,-1]])
    factor = 1.0
    bias = 0.0
    img = convolucion(imagen,aplica,matriz,factor,bias)
    return img

def sharpen2(imagen,aplica):

    matriz = np.matrix([[-1,-1,-1,-1,-1]
                      , [-1, 2, 2, 2,-1]
                      , [-1, 2, 8, 2,-1]
                      , [-1, 2, 2, 2,-1]
                      , [-1,-1,-1,-1,-1]])
    factor = 1.0/8.0
    bias = 0.0
    img = convolucion(imagen,aplica,matriz,factor,bias)
    return img

def sharpen3(imagen,aplica):

    matriz = np.matrix([[1, 1,1]
                      , [1,-7,1]
                      , [1, 1,1]])
    factor = 1.0
    bias = 0.0
    img = convolucion(imagen,aplica,matriz,factor,bias)
    return img

def emboss1(imagen,aplica):

    matriz = np.matrix([[-1,-1, 0]
                      , [-1, 0, 1]
                      , [ 0, 1, 1]])
    factor = 1.0
    bias = 128.0
    img = convolucion(imagen,aplica,matriz,factor,bias)
    return img

def emboss2(imagen,aplica):

    matriz = np.matrix([[-1,-1,-1,-1, 0]
                      , [-1,-1,-1, 0, 1]
                      , [-1,-1, 0, 1, 1]
                      , [-1, 0, 1, 1, 1]
                      , [ 0, 1, 1, 1, 1]])
    factor = 1.0
    bias = 128.0
    img = convolucion(imagen,aplica,matriz,factor,bias)
    return img
    
def convolucion(imagen,aplica,matriz,factor,bias):
    ancho = imagen.size[0]
    alto = imagen.size[1]
    rgb = imagen.convert('RGB')
    pixels = aplica.load()
    x,y = matriz.shape

    for i in range(ancho):
        for j in range(alto):
            rojo = 0.0
            verde = 0.0
            azul = 0.0
            for k in range(x):
                for l in range (y):
                    imageX = (i - x / 2 + k + ancho) % ancho
                    imageY = (j - y / 2 + l + alto) % alto
                    r,g,b = rgb.getpixel((imageX,imageY))
                    valor = matriz.item((k,l))
                    rojo += r * valor
                    verde += g * valor
                    azul += b * valor

            red = min(max((factor * rojo + bias),0),255)
            green = min(max((factor * verde + bias),0),255)
            blue = min(max((factor * azul + bias),0),255)
            pixels[i,j] = (int(red),int(green),int(blue))

    return aplica
            
