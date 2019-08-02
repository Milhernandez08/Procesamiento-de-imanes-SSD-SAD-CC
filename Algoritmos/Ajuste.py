from AreaNucleo import AreaNucleo
from ALGALI import Alineacion
from ALGSSD import SSD
from time import time
import cv2.cv2 as cv
import numpy as np
import math
#============= CONVERTIR A ESCALA DE GRISES ============
imges = cv.cvtColor(cv.imread('Images/Gal.jpeg'), cv.COLOR_BGR2GRAY)

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
'''
cv.imshow('parte', parteImg)
cv.waitKey(0)
cv.destroyAllWindows()'''

ejes = AreaNucleo().coordenadaApertura(imges, x, y) # y_Arri, y_Abaj, x_Izq, x_Der

ejeY = ejes[0]
ejeX = ejes[1]

coordenadas = SSD().coordenadas(imges, parteImg, ejes)
Alineacion = Alineacion().imgAlieada(imges, coordenadas, y, x)

print(Alineacion)
'''
newimg = np.zeros((len(imges), len(imges[0])), dtype=int)

imges = np.array(imges)

Y = y - coordenadas[0]
X = x - coordenadas[1]

print(Y,X)
#============= VALIDACIONES ============

yi = 0
yf = 0

xi = 0
xf = 0

if Y >= 0:
    yi = 0
    yf = len(imges) - Y
else:
    yi = int(math.fabs(Y))
    yf = len(imges)


if X >= 0:
    xi = 0
    xf = len(imges[0]) - X
else:
    xi = int(math.fabs(X))
    xf = len(imges[0])

print("X->", X)
print("--------------------------")
#print( imges[ yi:yf, xi:xf ] )

ymi = 0
ymf = 0
xmi = 0
xmf = 0
if X < 0:
    xmi = int(math.fabs(X)) - int(math.fabs(X))
    xmf = len(imges[0]) - int(math.fabs(X))
else:
    xmi = int(math.fabs(X))
    xmf = len(imges[0])

if Y < 0:
    ymi = int(math.fabs(Y)) - int(math.fabs(Y))
    ymf = len(imges) - int(math.fabs(Y))
else:
    ymi = int(math.fabs(Y))
    ymf = len(imges)

print(yi,yf,xi,xf)
print(ymi,ymf,xmi,xmf)

newimg[ ymi:ymf, xmi:xmf ] = imges[ yi:yf, xi:xf ]

#newimg[ 270:273, 181:184 ] = imges[ 270:273, 181:184   ]
print(imges.shape)

for i in newimg:
    print(i)
#newimg[272][183] = imges[0][0]


'''



















'''
img = cv.imread('Images/Gal.jpeg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('color', img)
cv.imshow('grus', img_gray)

print("VALORES DE LA IMAGEN ORIGINAL")
print(img)
print("IMAGEN ORIGINAL n FILAS, n COLUMNAS Y ")
print(img.shape)
print("IMAGEN EN ESCALA DE GRISES")
print(img_gray.shape)

cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)
'''
'''
imgnew = np.zeros((9,9))

imges = []
aux = []
x  = 0
for i in range(1,10):
    for j in range(1,10):
        x += 1
        aux.append(x)
    imgpaso.append(aux)
    aux = []

imgpaso = np.array(imgpaso)

original = [4,5]
corimg = [6,3]

y = original[0]-corimg[0]
x = original[1]-corimg[1]

print(y,x)
#============= VALIDACIONES ============

yi = 0
yf = 0

xi = 0
xf = 0

if y >= 0:
    yi = 0
    yf = len(imgpaso) - y
else:
    yi = int(math.fabs(y))
    yf = len(imgpaso)


if x >= 0:
    xi = 0
    xf = len(imgpaso) - x
else:
    xi = int(math.fabs(x))
    xf = len(imgpaso[0])


print(imgpaso)
print (yi, yf)
print (xi, xf)
print("--------------------------")
print( imgpaso[ yi:yf, xi:xf ] )

ymi = 0
ymf = 0
xmi = 0
xmf = 0
if x < 0:
    xmi = int(math.fabs(x)) - int(math.fabs(x))
    xmf = len(imgpaso[0]) - int(math.fabs(x))
else:
    xmi = int(math.fabs(x))
    xmf = len(imgpaso[0])

if y < 0:
    ymi = int(math.fabs(y)) - int(math.fabs(y))
    ymf = len(imgpaso) - int(math.fabs(y))
else:
    ymi = int(math.fabs(y))
    ymf = len(imgpaso)

imgnew[ ymi:ymf, xmi:xmf ] = imgpaso[ yi:yf, xi:xf ]
print(imgnew)
'''
