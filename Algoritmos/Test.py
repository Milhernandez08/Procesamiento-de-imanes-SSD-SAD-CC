from AreaNucleo import AreaNucleo
from ALGALI import Alineacion
from ALGSSD import SSD
from time import time
import cv2.cv2 as cv
import numpy as np

imges = cv.cvtColor(cv.imread('im000001.jpg'), cv.COLOR_BGR2GRAY)

cv.imshow('original', imges)

cv.waitKey(0)
cv.destroyAllWindows()
'''
ejes = AreaNucleo().validacion_ejeX(imges, 50, 49, 99, 239)
print (ejes)
'''

y = int ( input ("Ingrese el valor de Y: "))
x = int ( input ("Ingrese el valor de x: "))

parteImg = np.array(imges[y-7:y+4, x-6:x+5])

cv.imshow('parte', parteImg)

cv.waitKey(0)
cv.destroyAllWindows()

start_time = time()
img = []
for i in range (2,101):
    if i <= 9:
        img = cv.cvtColor(cv.imread('im00000'+str(i)+'.jpg'), cv.COLOR_BGR2GRAY)
    elif i <= 99:
        img = cv.cvtColor(cv.imread('im0000'+str(i)+'.jpg'), cv.COLOR_BGR2GRAY)
    elif i <= 999:
        img = cv.cvtColor(cv.imread('im000'+str(i)+'.jpg'), cv.COLOR_BGR2GRAY)
    else:
        img = cv.cvtColor(cv.imread('im00'+str(i)+'.jpg'), cv.COLOR_BGR2GRAY)

    ejes = AreaNucleo().coordenadaApertura(img, x, y) # y_Arri, y_Abaj, x_Izq, x_Der

    ejeY = ejes[0]
    ejeX = ejes[1]

    #imgArea = img[ejeY[0]:ejeY[1], ejeX[0]:ejeX[1]]

    coordenadas = SSD().coordenadas(img, parteImg, ejes)
    print (i)
    print ( "Y: ", y, "\tNY: ",coordenadas[0], "\t\tRESTA: mvY:", y-coordenadas[0], "mvX:", x-coordenadas[1],"\n", "X: ", x, "\tNX: ", coordenadas[1], "\n\n" )

    imgAlineada = Alineacion().imgAlieada(img, coordenadas, y, x)
elapsed_time = time() - start_time

print('\n\n', elapsed_time)