from PIL import ImageTk, Image

class Imagen():

    """
    Constructor de la clase Imagen
    Recibe la ruta de la imagen
    La imagen recibida se escala a 500x500 pixeles
    """
    def __init__(self,ruta):
        size = 500,500
        self.imagen = Image.open(ruta)
        self.aplica = Image.open(ruta)
        self.imagen.thumbnail(size,Image.ANTIALIAS)
        self.aplica.thumbnail(size,Image.ANTIALIAS)

    """
    Funcion para obtener la imagen original
    """
    def getImagen(self):
        return self.imagen

    """
    Funcion para obtener la imagen a la que se le aplicara el filtro
    """
    def getAplica(self):
        return self.aplica

