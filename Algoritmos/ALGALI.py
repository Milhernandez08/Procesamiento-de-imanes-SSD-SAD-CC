import numpy as np
import math

class Alineacion:
    def imgAlieada(self, imgRecorrido, cSSD, Y, X):
        imgNueva = np.zeros((len(imgRecorrido), len(imgRecorrido[0])))                    
        imgPaso = np.array(imgRecorrido)
        y = Y - cSSD[0]
        x = X - cSSD[1]

        yi = 0
        yf = 0
        xi = 0
        xf = 0

        if y >= 0:
            yi = 0
            yf = len(imgPaso) - y
        else:
            yi = int(math.fabs(y))
            yf = len(imgPaso)

        if x >= 0:
            xi = 0
            xf = len(imgPaso[0]) - x
        else:
            xi = int(math.fabs(x))
            xf = len(imgPaso[0])

        ymi = 0
        ymf = 0
        xmi = 0
        xmf = 0

        if x < 0:
            xmi = int(math.fabs(x)) - int(math.fabs(x))
            xmf = len(imgPaso[0]) - int(math.fabs(x))
        else:
            xmi = int(math.fabs(x))
            xmf = len(imgPaso[0])

        if y < 0:
            ymi = int(math.fabs(y)) - int(math.fabs(y))
            ymf = len(imgPaso) - int(math.fabs(y))
        else:
            ymi = int(math.fabs(y))
            ymf = len(imgPaso)

        imgNueva[ ymi:ymf, xmi:xmf ] = imgPaso[ yi:yf, xi:xf ]

        return imgNueva

        '''
        ejeY = self.validacionY(imgPaso, y)
        ejeX = self.validacionX(imgPaso, x)

        print (ejeY)
        print (ejeX)
        imgNueva[ ejeY[2]:ejeY[3], ejeX[2]:ejeX[3] ] = imgPaso [ ejeY[0]:ejeY[1], ejeX[0]:ejeX[1] ]
        #imgNueva[0][0] = imgRecorrido[0][0]

        return imgNueva

    def validacionY(self, imgPaso, y):
        ejesDeY = []

        if y >= 0:
            ejesDeY.append(0)
            ejesDeY.append(len(imgPaso) - y)
            ejesDeY.append(int(math.fabs(y)))
            ejesDeY.append(len(imgPaso))
        else:
            ejesDeY.append(int(math.fabs(y)))
            ejesDeY.append(len(imgPaso))
            ejesDeY.append(int(math.fabs(y)) - int(math.fabs(y)))
            ejesDeY.append(len(imgPaso) - int(math.fabs(y)))
        return ejesDeY

    def validacionX(self, imgPaso, x):
        ejesDeX = []

        if x >= 0:
            ejesDeX.append(0)
            ejesDeX.append(len(imgPaso) - x)
            ejesDeX.append(int(math.fabs(x)))
            ejesDeX.append(len(imgPaso[0]))
        else:
            ejesDeX.append(int(math.fabs(x)))
            ejesDeX.append(len(imgPaso[0]))
            ejesDeX.append(int(math.fabs(x)) - int(math.fabs(x)))
            ejesDeX.append(len(imgPaso[0]) - int(math.fabs(x)))
        return ejesDeX
        '''
