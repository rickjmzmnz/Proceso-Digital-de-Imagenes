import tkFileDialog
import types
from Tkinter import *
import tkMessageBox
from PIL import ImageTk, Image
import os
from Imagen import *
from TonosGris import *
from FiltrosColores import *
from FiltroBrillo import *
from AltoContraste import *
from FiltroMosaico import *
from FiltroWarhol import *
from Convolucion import *
from QuitarMarca import *
from Letras import *
from Recursiva import *

class Interfaz(Frame):

    #Variable global que usaremos para crea un objeto de la clase Imagen
    global image
    
    """
    Constructor de la clase
    Manda a llamar el constructor de la clase Frame
    Se inicializan las variables imagen y aplicar para asignarles las imagenes
    Se crean los canvas y el menu
    """
    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.pack(fill=BOTH, expand=True)
        self.imagen = None
        self.aplica = None
        self.creaCanvas()
        self.creaMenu()

    """    
    Funcion para crear las pestanas del menu
    Se definen tres pestanas
    La primera es para abrir una imagen
    La segunda es la que nos da la opcion de aplicar filtros
    La tercera es para salir del programa
    """
    def creaMenu(self):

        self.menuBar = Menu(self)
        
        self.archivoMenu = Menu(self.menuBar, tearoff=0)
        self.archivoMenu.add_command(label="Abrir", command=self.escogerImagen)
        self.archivoMenu.add_command(label="Guardar", command=self.preguntaGuardar)
        
        self.menuBar.add_cascade(label="Imagen", menu=self.archivoMenu)

        self.filtroMenu = Menu(self.menuBar, tearoff=0)
        self.filtroMenu.add_command(label="Filtro rojo", command = lambda: self.aplicaFiltro(1))
        self.filtroMenu.add_command(label="Filtro azul", command = lambda: self.aplicaFiltro(2))
        self.filtroMenu.add_command(label="Filtro verde", command = lambda: self.aplicaFiltro(3))

        self.tonosGris = Menu(self.filtroMenu, tearoff=0)
        self.tonosGris.add_command(label="Tono gris 1", command= lambda: self.aplicaFiltro(4))
        self.tonosGris.add_command(label="Tono gris 2", command = lambda: self.aplicaFiltro(5))
        self.tonosGris.add_command(label="Tono gris 3", command = lambda: self.aplicaFiltro(6))
        self.tonosGris.add_command(label="Tono gris 4", command = lambda: self.aplicaFiltro(7))
        self.tonosGris.add_command(label="Tono gris 5", command = lambda: self.aplicaFiltro(8))
        self.tonosGris.add_command(label="Tono gris 6", command = lambda: self.aplicaFiltro(9))
        self.tonosGris.add_command(label="Tono gris 7", command = lambda: self.aplicaFiltro(10))
        self.tonosGris.add_command(label="Tono gris 8", command = lambda: self.aplicaFiltro(11))
        self.filtroMenu.add_cascade(label="Tonos de gris", menu=self.tonosGris)

        self.filtroMenu.add_command(label="Filtro azar", command = lambda: self.aplicaFiltro(12))
        self.filtroMenu.add_command(label="Filtro brillo", command = self.aplicaBrillo)
        self.filtroMenu.add_command(label="Filtro alto contraste", command = self.escogeGris)
        self.filtroMenu.add_command(label="Filtro inverso (alto contraste)", command = self.escogeGrisInverso)
        self.filtroMenu.add_command(label="Filtro mosaico", command = lambda: self.aplicaMosaico(1))
        self.filtroMenu.add_command(label="Filtro warhol", command = self.aplicaWarhol)
        self.filtroMenu.add_command(label="Quitar marca de agua", command = lambda: self.aplicaFiltro(13))
        self.filtroMenu.add_command(label="Recursiva gris", command = lambda: self.aplicaMosaico(2))
        self.filtroMenu.add_command(label="Recursiva color", command = lambda: self.aplicaMosaico(3))
        
        self.convolucionMenu = Menu(self.menuBar, tearoff=0)

        self.blur = Menu(self.convolucionMenu, tearoff=0)
        self.blur.add_command(label="Blur 1", command = lambda: self.aplicaConvolucion(1))
        self.blur.add_command(label="Blur 2", command = lambda: self.aplicaConvolucion(2))
        self.convolucionMenu.add_cascade(label="Filtro blur", menu=self.blur)
        self.convolucionMenu.add_command(label="Filtro motion blur", command = lambda: self.aplicaConvolucion(3))
        self.bordes = Menu(self.convolucionMenu, tearoff=0)
        self.bordes.add_command(label="Encuentra bordes 1", command = lambda: self.aplicaConvolucion(4))
        self.bordes.add_command(label="Encuentra bordes 2", command = lambda: self.aplicaConvolucion(5))
        self.bordes.add_command(label="Encuentra bordes 3", command = lambda: self.aplicaConvolucion(6))
        self.bordes.add_command(label="Encuentra bordes 4", command = lambda: self.aplicaConvolucion(7))
        self.convolucionMenu.add_cascade(label="Filtro encuentra bordes", menu=self.bordes)
        self.sharpen = Menu(self.convolucionMenu, tearoff=0)
        self.sharpen.add_command(label="Sharpen 1", command = lambda : self.aplicaConvolucion(8))
        self.sharpen.add_command(label="Sharpen 2", command = lambda : self.aplicaConvolucion(9))
        self.sharpen.add_command(label="Sharpen 3", command = lambda : self.aplicaConvolucion(10))
        self.convolucionMenu.add_cascade(label="Filtro sharpen", menu=self.sharpen)
        self.emboss = Menu(self.convolucionMenu, tearoff=0)
        self.emboss.add_command(label="Emboss 1", command = lambda : self.aplicaConvolucion(11))
        self.emboss.add_command(label="Emboss 2", command = lambda : self.aplicaConvolucion(12))
        self.convolucionMenu.add_cascade(label="Filtro emboss", menu=self.emboss)

        self.letraMenu = Menu(self.menuBar, tearoff=0)
        self.letraMenu.add_command(label="Colores", command = lambda: self.aplicaLetra(1))
        self.letraMenu.add_command(label="Gris", command = lambda: self.aplicaLetra(2))
        self.letraMenu.add_command(label="Simbolos", command = lambda: self.aplicaLetra(8))
        self.letraMenu.add_command(label="SimbolosGris", command = lambda: self.aplicaLetra(3))
        self.letraMenu.add_command(label="SimbolosColor", command = lambda: self.aplicaLetra(4))
        self.letraMenu.add_command(label="Palabra", command = self.aplicaPalabra)
        self.letraMenu.add_command(label="Naipes", command = lambda: self.aplicaLetra(5))
        self.letraMenu.add_command(label="Domino Negro", command = lambda: self.aplicaLetra(6))
        self.letraMenu.add_command(label="Domino Blanco", command = lambda: self.aplicaLetra(7))
        
        self.menuBar.add_cascade(label="Filtros", menu=self.filtroMenu)

        self.menuBar.add_cascade(label="Convolucion", menu=self.convolucionMenu)

        self.menuBar.add_cascade(label="Letras", menu=self.letraMenu)

        self.menuBar.add_command(label="Salir", command = self.salir)
        
        root.config(menu=self.menuBar)

    """
    Funcion para crear los canvas
    Se crea un canvas izquierdo y derecho 
    """
    def creaCanvas(self):

        self.originalVentana = Canvas(self, bg="white",width=500,height=400)
        self.originalVentana.pack(side=LEFT, fill=BOTH, expand=True)
        
        self.filtroVentana = Canvas(self,bg ="white",width=500,height=400 )
        self.filtroVentana.pack(side=RIGHT, fill=BOTH, expand=True)

    """
    Funcion para salir del programa
    """
    def salir(self):
        os._exit(0)
        
    """
    Ventana emergente para mostrar los formatos en el que se puede guardar la imagen
    """
    def preguntaGuardar(self):
        if self.filtroVentana.find_all() != ():
            self.top = Toplevel()

            self.label = Label (self.top, text= "Puedes guardar la imagen en formato jpg o png")
            self.label.pack()

            self.buttontext = StringVar()
            self.buttontext.set("Guardar")
            self.button = Button(self.top, textvariable=self.buttontext, command= self.guardarImagen).pack()
        else:
            tkMessageBox.showwarning("Error","No hay imagen")

    """
    Funcion para guardar la imagen con el filtro aplicado
    """
    def guardarImagen(self):
        self.nuevaImagen.save(tkFileDialog.asksaveasfilename())
        self.top.destroy()
   
    """
    Funcion para colocar las imagenes en los canvas
    Pregunta por la imagen que se desea abrir
    Se colocan dos imagenes iguales
    En el canvas izquierdo se va a mantener la imagen original
    En el canvas derecho se coloca la imagen que se le aplicaran los filtros
    """
    def escogerImagen(self):
        
        ruta = tkFileDialog.askopenfilename()
        image = Imagen(ruta)
        self.imagen = image.getImagen()
        self.aplica = image.getAplica()
        
        imageFile = ImageTk.PhotoImage(self.imagen)
        imageAplica = ImageTk.PhotoImage(self.aplica)

        self.originalVentana.image = imageFile
        self.originalVentana.create_image(imageFile.width()/2, imageFile.height()/2, anchor=CENTER, image=imageFile, tags="bg_img")

        self.filtroVentana.image = imageAplica
        self.filtroVentana.create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")

        self.originalVentana.create_text((250,380),text="Imagen original")
        self.filtroVentana.create_text((250,380),text="Imagen con filtro")
            
    """
    Funcion para seleccionar que filtro aplicar
    Dado un entero se decide que filtro aplicaremos a la imagen
    """
    def aplicaFiltro(self,opcion):

        if self.filtroVentana.find_all() != ():
            if opcion == 1:
                self.nuevaImagen = filtroRojo(self.imagen,self.aplica)
            elif opcion == 2:
                self.nuevaImagen = filtroAzul(self.imagen,self.aplica)
            elif opcion == 3:
                self.nuevaImagen = filtroVerde(self.imagen,self.aplica)
            elif opcion == 4:
                self.nuevaImagen = filtroGris1(self.imagen,self.aplica)
            elif opcion == 5:
                self.nuevaImagen = filtroGris2(self.imagen,self.aplica)
            elif opcion == 6:
                self.nuevaImagen = filtroGris3(self.imagen,self.aplica)
            elif opcion == 7:
                self.nuevaImagen = filtroGris4(self.imagen,self.aplica)
            elif opcion == 8:
                self.nuevaImagen = filtroGris5(self.imagen,self.aplica)
            elif opcion == 9:
                self.nuevaImagen = filtroGris6(self.imagen,self.aplica)
            elif opcion == 10:
                self.nuevaImagen = filtroGris7(self.imagen,self.aplica)
            elif opcion == 11:
                self.nuevaImagen = filtroGris8(self.imagen,self.aplica)
            elif opcion == 12:
                self.nuevaImagen = filtroAzar(self.imagen,self.aplica)
            elif opcion == 13:
                self.nuevaImagen = quitarMarca(self.imagen,self.aplica)
            imageAplica = ImageTk.PhotoImage(self.nuevaImagen)
            self.filtroVentana.image = imageAplica
            self.filtroVentana.create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")
        else:
            tkMessageBox.showwarning("Error","Escoge una imagen antes de aplicar un filtro")

    """
    Ventana emergente para indicar que se espere mientras se aplica el filtro
    """
    def aplicaConvolucion(self,valor):
        if self.filtroVentana.find_all() != ():
            self.top = Toplevel()

            self.label = Label (self.top, text= "El filtro puede tardar un poco en aplicarse")
            self.label.pack()

            self.buttontext = StringVar()
            self.buttontext.set("Aplicar filtro")
            self.button = Button(self.top, textvariable=self.buttontext, command= lambda: self.asignaConvolucion(valor)).pack()
        else:
            tkMessageBox.showwarning("Error","Escoge una imagen antes de aplicar un filtro")


    def asignaConvolucion(self,valor):
        if valor == 1:
            self.nuevaImagen = blur1(self.imagen,self.aplica)
        elif valor == 2:
            self.nuevaImagen = blur2(self.imagen,self.aplica)
        elif valor == 3:
            self.nuevaImagen = motionBlur(self.imagen,self.aplica)
        elif valor == 4:
            self.nuevaImagen = encuentraBordes1(self.imagen,self.aplica)
        elif valor == 5:
            self.nuevaImagen = encuentraBordes2(self.imagen,self.aplica)
        elif valor == 6:
            self.nuevaImagen = encuentraBordes3(self.imagen,self.aplica)
        elif valor == 7:
            self.nuevaImagen = encuentraBordes4(self.imagen,self.aplica)
        elif valor == 8:
            self.nuevaImagen = sharpen1(self.imagen,self.aplica)
        elif valor == 9:
            self.nuevaImagen = sharpen2(self.imagen,self.aplica)
        elif valor == 10:
            self.nuevaImagen = sharpen3(self.imagen,self.aplica)
        elif valor == 11:
            self.nuevaImagen = emboss1(self.imagen,self.aplica)
        elif valor == 12:
            self.nuevaImagen = emboss2(self.imagen,self.aplica)
        imageAplica = ImageTk.PhotoImage(self.nuevaImagen)
        self.filtroVentana.image = imageAplica
        self.filtroVentana.create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")
        self.top.destroy()
        
    """
    Ventana emergente para aplicar la cantidad de brillo a la imagen al aplicar el filtro brillo
    """
    def aplicaBrillo(self):
        if self.filtroVentana.find_all() != ():
            self.top = Toplevel()

            self.label = Label (self.top, text= "Introduce la cantidad de brillo que quieres\nTiene que ser un valor entre -128 y 128.")
            self.label.pack()

            self.entrytext = IntVar()
            Entry(self.top, textvariable=self.entrytext).pack()

            self.buttontext = StringVar()
            self.buttontext.set("Aplica Brillo")
            self.button = Button(self.top, textvariable=self.buttontext, command= lambda: self.sacaValor(self.entrytext)).pack()
        else:
            tkMessageBox.showwarning("Error","Escoge una imagen antes de aplicar un filtro")
            
    """
    Al colocar un valor en la pantalla emergente para el brillo
    Ese valor se le pasa a la funcion de filtroBrillo
    """
    def sacaValor(self,valor):
        
        self.entrytext = valor.get()
        self.nuevaImagen = filtroBrillo(self.imagen,self.aplica,self.entrytext)
        imageAplica = ImageTk.PhotoImage(self.nuevaImagen)
        self.filtroVentana.image = imageAplica
        self.filtroVentana.create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")
        self.top.destroy()

    """
    Ventana emergente para dar los tres valores rojo,verde y azul para aplicar el filtro Warhol
    """
    def aplicaWarhol(self):
        if self.filtroVentana.find_all() != ():
            
            self.top = Toplevel()

            self.label = Label (self.top, text= "Introduce los tres valores para rojo, verde y azul\nTienen que ser un valores entre 0 y 255.")
            self.label.pack()

            self.entraRojo = IntVar()
            Entry(self.top, textvariable=self.entraRojo).pack()

            self.entraVerde = IntVar()
            Entry(self.top, textvariable=self.entraVerde).pack()

            self.entraAzul = IntVar()
            Entry(self.top, textvariable=self.entraAzul).pack()

            self.buttontext = StringVar()
            self.buttontext.set("Aplica Warhol")
            self.button = Button(self.top, textvariable=self.buttontext, command= lambda: self.obtenWarhol(self.entraRojo,self.entraVerde,self.entraAzul)).pack()
        else:
            tkMessageBox.showwarning("Error","Escoge una imagen antes de aplicar un filtro")

    """
    Al colocar los tres valores en la ventana emergente de aplicaWarhol
    Esos valores se le pasan a la funcion filtroWarhol
    """
    def obtenWarhol(self,valorRojo,valorVerde,valorAzul):
        
        self.entraRojo = valorRojo.get()
        self.entraVerde = valorVerde.get()
        self.entraAzul = valorAzul.get()
        self.nuevaImagen = filtroWarhol(self.imagen,self.aplica,self.entraRojo,self.entraVerde,self.entraAzul)
        imageAplica = ImageTk.PhotoImage(self.nuevaImagen)
        self.filtroVentana.image = imageAplica
        self.filtroVentana.create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")
        self.top.destroy()

    """
    Ventana emergente para escoger el tono de gris para el fitro Altro Contraste
    """
    def escogeGris(self):
        if self.filtroVentana.find_all() != ():
            self.top = Toplevel()

            self.label = Label (self.top, text= "Introduce que tono de gris quieres para el filtro, un valor entre 1 y 8")
            self.label.pack()

            self.entraGris = IntVar()
            Entry(self.top, textvariable=self.entraGris).pack()

            self.buttontext = StringVar()
            self.buttontext.set("Aplica Brillo")
            self.button = Button(self.top, textvariable=self.buttontext, command= lambda: self.daleTonoGrisContraste(self.entraGris)).pack()
        else:
            tkMessageBox.showwarning("Error","Escoge una imagen antes de aplicar un filtro")

    """
    Ya que se escogio el tono de gris
    Se toma la imagen, le aplicamos el filtro gris seleccionado
    Y esa nueva imagen se la damos al filtroAltoContraste
    """
    def daleTonoGrisContraste(self,gris):
        self.entraGris = gris.get()
        if(self.entraGris < 1 or self.entraGris > 8):
            tkMessageBox.showwarning("Error","Escoge un valor valido entre 1 y 8")
            self.top.destroy()
        else:
            if(self.entraGris == 1):
                imagenGris = filtroGris1(self.imagen,self.aplica)
            if(self.entraGris == 2):
                imagenGris = filtroGris2(self.imagen,self.aplica)
            if(self.entraGris == 3):
                imagenGris = filtroGris3(self.imagen,self.aplica)
            if(self.entraGris == 4):
                imagenGris = filtroGris4(self.imagen,self.aplica)
            if(self.entraGris == 5):
                imagenGris = filtroGris5(self.imagen,self.aplica)
            if(self.entraGris == 6):
                imagenGris = filtroGris6(self.imagen,self.aplica)
            if(self.entraGris == 7):
                imagenGris = filtroGris7(self.imagen,self.aplica)
            if(self.entraGris == 8):
                imagenGris = filtroGris8(self.imagen,self.aplica)
            self.nuevaImagen = filtroAltoContraste(imagenGris,self.aplica)
            imageAplica = ImageTk.PhotoImage(self.nuevaImagen)
            self.filtroVentana.image = imageAplica
            self.filtroVentana.create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")
            self.top.destroy()

    """
    Ventana emergente para escoger el tono de gris para el fitro Inverso
    """
    def escogeGrisInverso(self):
        if self.filtroVentana.find_all() != ():
            self.top = Toplevel()

            self.label = Label (self.top, text= "Introduce que tono de gris quieres para el filtro, un valor entre 1 y 8")
            self.label.pack()

            self.entraGris = IntVar()
            Entry(self.top, textvariable=self.entraGris).pack()

            self.buttontext = StringVar()
            self.buttontext.set("Aplica Brillo")
            self.button = Button(self.top, textvariable=self.buttontext, command= lambda: self.daleTonoGrisInverso(self.entraGris)).pack()
        else:
            tkMessageBox.showwarning("Error","Escoge una imagen antes de aplicar un filtro")

    """
    Ya que se escogio el tono de gris
    Se toma la imagen, le aplicamos el filtro gris seleccionado
    Y esa nueva imagen se la damos al filtroInverso
    """
    def daleTonoGrisInverso(self,gris):
        self.entraGris = gris.get()
        if(self.entraGris < 1 or self.entraGris > 8):
            tkMessageBox.showwarning("Error","Escoge un valor valido entre 1 y 8")
            self.top.destroy()
        else:
            if(self.entraGris == 1):
                imagenGris = filtroGris1(self.imagen,self.aplica)
            if(self.entraGris == 2):
                imagenGris = filtroGris2(self.imagen,self.aplica)
            if(self.entraGris == 3):
                imagenGris = filtroGris3(self.imagen,self.aplica)
            if(self.entraGris == 4):
                imagenGris = filtroGris4(self.imagen,self.aplica)
            if(self.entraGris == 5):
                imagenGris = filtroGris5(self.imagen,self.aplica)
            if(self.entraGris == 6):
                imagenGris = filtroGris6(self.imagen,self.aplica)
            if(self.entraGris == 7):
                imagenGris = filtroGris7(self.imagen,self.aplica)
            if(self.entraGris == 8):
                imagenGris = filtroGris8(self.imagen,self.aplica)
            self.nuevaImagen = filtroInverso(imagenGris,self.aplica)
            imageAplica = ImageTk.PhotoImage(self.nuevaImagen)
            self.filtroVentana.image = imageAplica
            self.filtroVentana.create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")
            self.top.destroy()

        
    """
    Ventana emergente para dar el tamanio del mosaico para el filtro mosaico
    """
    def aplicaMosaico(self,opcion):
        if self.filtroVentana.find_all() != ():
            
            self.top = Toplevel()
            
            self.label = Label (self.top, text= "Introduce el tamanio del mosaico\nDa dos valores positivos para (x,y) ")
            self.label.pack()

            self.entraX = IntVar()
            Entry(self.top, textvariable=self.entraX).pack()

            self.entraY = IntVar()
            Entry(self.top, textvariable=self.entraY).pack()

            self.label2 = Label (self.top, text= "Advertencia, el filtro puede tardar en aplicarse ")
            self.label2.pack()

            self.buttontext = StringVar()
            self.buttontext.set("Aplica mosaico")
            self.button = Button(self.top, textvariable=self.buttontext, command= lambda: self.obtenMosaico(self.entraX,self.entraY,opcion)).pack()
        else:
            tkMessageBox.showwarning("Error","Escoge una imagen antes de aplicar un filtro")

        """
    Al colocar los dos valores en la ventana emergente de aplicaMosaico
    Esos valores se le pasan a la funcion filtroMosaico
    """
    def obtenMosaico(self,valorX,valorY,opcion):        
        self.entraX = valorX.get()
        self.entraY = valorY.get()
        if(opcion == 1):
            self.nuevaImagen = filtroMosaico(self.imagen,self.aplica,self.entraX,self.entraY)
        elif(opcion == 2):
            generaImagenesGris(self.imagen,self.aplica)
            self.nuevaImagen = aplicaRecursivaGris(self.imagen,self.aplica,self.entraX,self.entraY)
            eliminaImagenesGris()
        elif(opcion == 3):
            self.nuevaImagen = aplicaRecursivaColor(self.imagen,self.aplica,self.entraX,self.entraY)
        imageAplica = ImageTk.PhotoImage(self.nuevaImagen)
        self.filtroVentana.image = imageAplica
        self.filtroVentana.create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")
        self.top.destroy()

    """
    Ventana emergente para dar el tamanio del mosaico para el filtro de letras
    """
    def aplicaLetra(self,opcion):
        if self.filtroVentana.find_all() != ():
            
            self.top = Toplevel()

            self.label = Label (self.top, text= "Introduce el tamanio del mosaico\nDa dos valores positivos para (x,y) ")
            self.label.pack()

            self.entraX = IntVar()
            Entry(self.top, textvariable=self.entraX).pack()

            self.entraY = IntVar()
            Entry(self.top, textvariable=self.entraY).pack()

            self.text = Label (self.top, text="Dar un nombre al archivo html que se va a generar")
            self.text.pack()

            self.nombre = StringVar()
            Entry(self.top, textvariable=self.nombre).pack()

            self.buttontext = StringVar()
            self.buttontext.set("Genera imagen")
            
            self.button = Button(self.top, textvariable=self.buttontext, command= lambda: self.obtenLetra(self.entraX,self.entraY,self.nombre,opcion)).pack()
        else:
            tkMessageBox.showwarning("Error","Escoge una imagen antes de aplicar un filtro")

    """
    Con los valores de la ventana emergente y el nombre
    Se les pasa a alguna funcion de los filtros de letras
    """
    def obtenLetra(self,valorX,valorY,nombreA,opcion):
        self.entraX = valorX.get()
        self.entraY = valorY.get()
        self.nombre = nombreA.get()
        if(opcion == 1):
            letraColor(self.imagen,self.aplica,self.entraX,self.entraY,self.nombre)
        elif(opcion == 2):
            letraGris(self.imagen,self.aplica,self.entraX,self.entraY,self.nombre)
        elif(opcion == 3):
            simbolosGris(self.imagen,self.aplica,self.entraX,self.entraY,self.nombre)
        elif(opcion == 4):
            simbolosColor(self.imagen,self.aplica,self.entraX,self.entraY,self.nombre)
        elif(opcion == 5):
            naipes(self.imagen,self.aplica,self.entraX,self.entraY,self.nombre)
        elif(opcion == 6):
            dominoN(self.imagen,self.aplica,self.entraX,self.entraY,self.nombre)
        elif(opcion == 7):
            dominoB(self.imagen,self.aplica,self.entraX,self.entraY,self.nombre)
        elif(opcion == 8):
            simbolos(self.imagen,self.aplica,self.entraX,self.entraY,self.nombre)
        self.top.destroy()   

    """
    Ventana emergente para dar el tamanio del mosaico para el filtro de una cadena
    """
    def aplicaPalabra(self):
        if self.filtroVentana.find_all() != ():
            
            self.top = Toplevel()

            self.label = Label (self.top, text= "Introduce el tamanio del mosaico\nDa dos valores positivos para (x,y) ")
            self.label.pack()

            self.entraX = IntVar()
            Entry(self.top, textvariable=self.entraX).pack()

            self.entraY = IntVar()
            Entry(self.top, textvariable=self.entraY).pack()

            self.peticion = Label(self.top, text="Da una cadena para el filtro")
            self.peticion.pack()

            self.cadena = StringVar()
            Entry(self.top, textvariable=self.cadena).pack()

            self.text = Label (self.top, text="Dar un nombre al archivo html que se va a generar")
            self.text.pack()

            self.nombre = StringVar()
            Entry(self.top, textvariable=self.nombre).pack()

            self.buttontext = StringVar()
            self.buttontext.set("Genera imagen")
            
            self.button = Button(self.top, textvariable=self.buttontext, command= lambda: self.obtenPalabra(self.entraX,self.entraY,self.nombre,self.cadena)).pack()
        else:
            tkMessageBox.showwarning("Error","Escoge una imagen antes de aplicar un filtro")

    """
    Con los valores de la ventana emergente,el nombre y la cadena
    Se le pasa a la funcion palabra
    """
    def obtenPalabra(self,valorX,valorY,nombreA,cadenaA):
        self.entraX = valorX.get()
        self.entraY = valorY.get()
        self.nombre = nombreA.get()
        self.cadena = cadenaA.get()
        palabra(self.imagen,self.aplica,self.entraX,self.entraY,self.nombre,self.cadena)
        self.top.destroy()        
        
"""
Funcion main
Se crea un objeto de la clase Tk
Le ponemos titulo a la ventana
Creamos un objeto de nuestra clase Filtros
Y se ejecuta el programa
"""        
if __name__  == "__main__":
    root = Tk()
    root.title("Proceso Digital de Imagenes")
    root.wm_state("normal")
    app = Interfaz(root)
    root.mainloop()
