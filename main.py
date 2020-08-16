from  Color import * #se importa Color

if __name__ == '__main__': #
    ruta_imagen = input('Ingrese la ruta de la imagen: ') #se pide al usuario que ingrese la ruta completa de la imagen
    imagen = colorImage(ruta_imagen) #se hace un llamado a la clase y se ingresa como parámetro la ruta
    imagen.displayProperties() #se muestran las propiedades de la imagen
    imagen.makeGray() #se muestra la imagen en escala de grises
    imagen.colorizeRGB('red') #se muestra la imagen colorizada en rojo
    imagen.makeHue() #se muestra la imagen en tonos