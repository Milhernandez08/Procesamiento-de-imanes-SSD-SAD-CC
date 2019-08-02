class AreaNucleo:
    def coordenadaApertura(self, imgRecorridas, ejeX, ejeY):
        ampli_IZQ = 50 #Amplitud en Izquierda
        ampli_DER = 49 #Amplitud en Derecha
        tamaño = ampli_IZQ + ampli_DER # tamaño del area de recorrido = 99

        Y = self.validacion_ejeY(imgRecorridas, ampli_IZQ, ampli_DER, tamaño, ejeY)
        X = self.validacion_ejeX(imgRecorridas, ampli_IZQ, ampli_DER, tamaño, ejeX)

        return Y , X


    def validacion_ejeY(self, imgRecorridas, ampli_IZQ, ampli_DER, tamaño, ejeY):
        y_Arri = 0
        y_Abaj = 0

        if ejeY < ampli_IZQ:
            y_Abaj = tamaño
        elif ejeY+ampli_DER >= len(imgRecorridas):
            y_Abaj = len(imgRecorridas) - 1
            y_Arri = y_Abaj - tamaño
        else:
            y_Arri = ejeY - ampli_IZQ
            y_Abaj = ejeY + ampli_DER
        
        return y_Arri , y_Abaj
    
    def validacion_ejeX(self, imgRecorridas, ampli_IZQ, ampli_DER, tamaño, ejeX):
        x_Izq = 0
        x_Der = 0

        if ejeX < ampli_IZQ:
            x_Der = tamaño
        elif ejeX+ampli_DER >= len(imgRecorridas[0]):
            x_Der = len(imgRecorridas[0]) - 1
            x_Izq = x_Der - tamaño
        else:
            x_Izq = ejeX - ampli_IZQ
            x_Der = ejeX + ampli_DER
        
        return x_Izq , x_Der