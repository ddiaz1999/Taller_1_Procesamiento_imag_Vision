from  Color import *

#C:\lenna.png

if __name__ == '__main__':
    ruta_imagen = input('Ingrese la ruta de la imagen: ')
    imagen = colorImage(ruta_imagen)
    imagen.displayProperties()
    imagen.makeGray()
    imagen.colorizeRGB('red')
    imagen.makeHue()
   
