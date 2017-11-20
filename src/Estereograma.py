import string
import random

"""
Recibe un arhivo de texto donde esta la imagen
Y se crea el estereograma de esa imagen en un nuevo archivo de texto
"""
def estereograma(archivo,nombre):
    f = open(archivo,"r")
    g = open(nombre+".txt","w")
    lines = f.readlines()
    abc = string.letters
    sub = abc[26:]
    for i in lines:
        for j in i:
            rand = random.choice(sub)
            g.write(rand)
        g.write("\n")
    g.close()
