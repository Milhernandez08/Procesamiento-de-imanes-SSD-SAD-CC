import numpy as np
import math

class CC:
    def coordenadas(self, imgRecorrido, parteImg, EJES):
        ejeY = EJES[0]
        ejeX = EJES[1]

        return self.posNumeroMayor(imgRecorrido, ejeY, ejeX, parteImg)

    def matrizDePosicion(self, imgRecorrido, ejeY, ejeX, parteImg):
        imgRecortada = imgRecorrido[ejeY[0]:ejeY[1], ejeX[0]:ejeX[1]]       # IMAGEN RECORTADA PARA RECORRER
        # ULTIMO INDICE PARA EL RECORRIDO
        ultimoFil = ( len ( imgRecortada ) - len ( parteImg ) ) + ejeY[0]
        ultimoCol = ( len ( imgRecortada[0] ) - len ( parteImg ) ) + ejeX[0]

        centro = len ( parteImg )//2                                        # CENTRO DEL LA PARTE DE LA IMAGEN ORIGINAL

        # ARRAY PARA ALMACENAR NOS NUEVOS VALORES QUE SE OBTENDRAN
        contenido = np.zeros( ( len ( imgRecorrido ), len ( imgRecorrido[0] ) ), dtype=int )
        #for x in range ( len (contenido) ):
        #    contenido[x] = 100000

        # TAMAÑO DEL ARRAY DE LA PARTE DE LA IMAGEN
        TM = len ( parteImg )

        # DETECTAR LOS CAMBIOS A HACER Y ALMACENARLOS
        for fil in range (ejeY[0], ejeY[1]):
            for col in range (ejeX[0], ejeX[1]):
                multi = np.sum ( np.multiply ( parteImg, imgRecorrido[fil:fil+TM, col:col+TM] ) )
                contenido[fil + centro][col + centro] = multi
                
                if col == ultimoCol:
                    break
            if fil == ultimoFil:
                break
        
        return contenido
    
    def posNumeroMayor(self, imgRecorrido, ejeY, ejeX, parteImg):
        contenido = self.matrizDePosicion (imgRecorrido, ejeY, ejeX, parteImg)
        posicion = []
        valorPos = np.zeros((len(contenido)), dtype=int)
        i = 0
        for x in range ( len (contenido) ):
            posicion.append((x, contenido[x].argmax()))
            valorPos[i] = contenido[x, contenido[x].argmax()]
            i += 1
        return posicion[valorPos.argmax()]