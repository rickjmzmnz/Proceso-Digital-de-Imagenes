from PIL import ImageTk, Image

"""
Quita la marca de agua de imagenes en tonos de gris
Recorre la imagen
Omite los pixeles que esten en tono de gris
Encuentre los pixeles de la marca de agua
Hace la suma de los tres componentes, se divide entre 3 y se multiplica por una constante magica
Para quitar la marca de agua
"""
def quitarMarca(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()    
    for i in range(imagen.size[0]):
        for j in range(aplica.size[1]):
            r,g,b = rgb.getpixel((i,j))
            nr = (r - g)
            if(nr < 10):
                pass
            else:
                prom = (int)((1.3475)*((r+g+b)/3))
                pixels[i,j] = (prom,prom,prom,0)
    return aplica
    
