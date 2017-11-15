from PIL import Image,ImageTk
import binascii

def cifrar(imagen,mensaje):
    rgb = imagen.convert('RGB')
    ancho = imagen.size[0]
    alto = imagen.size[1]
    nueva = Image.new("RGB",(ancho,alto),"white")
    pixels = nueva.load()
    mensajeBin = ''.join(format(ord(x),'b') for x in mensaje)
    contador = 0
    for i in range(ancho):
        for j in range(alto):
            r,g,b = rgb.getpixel((i,j))
            rbyte = "{0:b}".format(r)
            rbyte = list(rbyte)
            gbyte = "{0:b}".format(g)
            gbyte = list(gbyte)
            bbyte = "{0:b}".format(b)
            bbyte = list(bbyte)
            if(contador < len(mensajeBin)):
                rbyte[len(rbyte)-1] = mensajeBin[contador]
                contador += 1
            if(contador < len(mensajeBin)):
                gbyte[len(gbyte)-1] = mensajeBin[contador]
                contador += 1
            if(contador < len(mensajeBin)):
                bbyte[len(bbyte)-1] = mensajeBin[contador]
                contador += 1
            r = "".join(rbyte)
            r = int(r,2)
            g = "".join(gbyte)
            g = int(g,2)
            b = "".join(bbyte)
            b = int(b,2)
            pixels[i,j] = (r,g,b)
    nueva.save("nuevaImagen.png","PNG")
    return imagen

def descifrar(imagen):
    rgb = imagen.convert("RGB")
    ancho = imagen.size[0]
    alto = imagen.size[1]
    mensaje = ""
    for i in range(ancho):
        for j in range(alto):
            r,g,b = rgb.getpixel((i,j))
            rbyte = "{0:b}".format(r)
            rbyte = list(rbyte)
            gbyte = "{0:b}".format(g)
            gbyte = list(gbyte)
            bbyte = "{0:b}".format(b)
            bbyte = list(bbyte)
            mensaje = mensaje + rbyte[len(rbyte)-1] + gbyte[len(gbyte)-1] + bbyte[len(bbyte)-1]
    print(chr(int(mensaje[:8],2)))
    return imagen
