import numpy as np
import cv2
import os

class colorImage:
    def __init__(self,path_file):
        self.image = cv2.imread(path_file,1)

    def displayProperties(self):
        print(f'El alto de la imagen es {self.image.shape[0]}. El ancho de la imagen es {self.image.shape[1]}')

    def makeGray(self):
        cv2.imshow('Gray Image',cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY))
        cv2.waitKey(0)

    def colorizeRGB(self,canal_de_color):
        if canal_de_color == 'blue':
            b = self.image.copy()
            b[:,:,1] = 0
            b[:,:,2] = 0
            cv2.imshow('Blue image',b)
            cv2.waitKey(0)

        if canal_de_color == 'red':
            r = self.image.copy()
            r[:,:,0] = 0
            r[:,:,1] = 0
            cv2.imshow('Red image',r)
            cv2.waitKey(0)

        if canal_de_color == 'green':
            g = self.image.copy()
            g[:,:,0] = 0
            g[:,:,2] = 0
            cv2.imshow('Green image',g)
            cv2.waitKey(0)

    def makeHue(self):
        HSV_Image = cv2.cvtColor(self.image,cv2.COLOR_BGR2HSV)
        HSV_Image[:,:,1] = 255
        HSV_Image[:,:,2] = 255
        HSV_Image = cv2.cvtColor(HSV_Image,cv2.COLOR_HSV2BGR)
        cv2.imshow('Imagen en tonos',HSV_Image)
        cv2.waitKey(0)
