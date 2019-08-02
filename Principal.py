import os, sys
import cv2.cv2 as cv
import numpy as np
from time import time
from matplotlib import pyplot as plt
import glob
from showIMG import *
from Algoritmos.AreaNucleo import AreaNucleo
from Algoritmos.ALGSSD import SSD
from Algoritmos.ALGALI import Alineacion
from Algoritmos.ALGSAD import SAD
from Algoritmos.ALGCC import CC

from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QProgressBar
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.Qt import QMovie
from decimal import Decimal
form_class = uic.loadUiType("algoritmos.ui")[0]

cap = cv.VideoCapture('ImgDiseño/video.mp4')
TIME_LIMIT = 100
class Principal(QtWidgets.QMainWindow, form_class):
    def __init__(self):
        super(Principal, self).__init__()
        # ======================= VARIABLES GLOBALES ===========================
        global imagen, img
        self.ejes = AreaNucleo()
        # ======================= VENTANA1 PRINCIPAL ===========================
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        # ======================= VENTANA2 IMAGENES ============================
        self.ventana2 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.ventana2)
        # ======================= SOQUEKETS DE CONECCIONES =====================
        self.connectActions()

    # ======================= CONECCIONES WIDGETS ============================
    def connectActions(self):
        self.btnSSD.clicked.connect(self.seleccionarImagen)        
        self.btnSAD.clicked.connect(self.seleccionarImagen)
        self.btnCC.clicked.connect(self.seleccionarImagen)
        self.ui.btnCoordenadas.clicked.connect(self.mostrarImagen)        
        self.ui.btnEcualizar.clicked.connect(self.ecualizacion)
        self.ui.btnEjecutar.clicked.connect(self.recivirDatos)

    # ======================= FUNCIONES ============================
    def seleccionarImagen(self):                
        print("Nombre button -> ",self.sender().text())
        self.nameButon = self.sender().text()
        self.imagen, extension = QFileDialog.getOpenFileName(self, "Seleccionar imagen", os.getcwd(),
                                                        "Archivos de imagen (*.png *.jpg *.jpeg)",
                                                        options=QFileDialog.Options())

        if self.imagen:
            # Adaptar imagen
            self.pixmapImagen = QPixmap(self.imagen).scaled(690, 440, Qt.KeepAspectRatio,Qt.SmoothTransformation)
            # Mostrar imagen
            self.ui.lblImg.setPixmap(self.pixmapImagen)
            self.movi = QMovie("ImgDiseño/imgEspera.gif")
            self.ui.lblImgEspera.setMovie(self.movi)
            self.movi.start()
            self.ventana2.show()

    def mostrarImagen(self, imagen):
        self.img = cv.cvtColor(cv.imread(self.imagen), cv.COLOR_BGR2GRAY)
        cv.imshow('Escoger coordenada', self.img)

    def recivirDatos(self):
        x = int(self.ui.editX.text())
        y = int(self.ui.editY.text())
        gama = float(self.ui.editBeta.text())
        mapa  = self.ejes.coordenadaApertura(self.img, x, y)
        nucleo = np.array(self.img[y-7:y+4, x-6:x+5])
        ejey = mapa[0] 
        ejex = mapa[1]
        #cv.imshow('Area busqueda', self.img[ejey[0]:ejey[1], ejex[0]:ejex[1]])
        #cv.imshow('Nucleo', nucleo)
        self.procesamiento(nucleo, y, x, gama)


    def procesamiento(self, nucleo, y, x, gama):
        shImg =  []
        canImg = int(self.ui.editCantImg.text()) + 2
        Fondo = np.zeros( (len(self.img), len(self.img[0])))
        coordenadas = []
        imgVideo = []
        timeEjecucion = 0.0
        start_time = time()
        for i in range (2,canImg):
            if i <= 9:
                img = cv.cvtColor(cv.imread('AlbumImages/im00000'+str(i)+'.jpg'), cv.COLOR_BGR2GRAY)
            elif i <= 99:
                img = cv.cvtColor(cv.imread('AlbumImages/im0000'+str(i)+'.jpg'), cv.COLOR_BGR2GRAY)
            elif i <= 999:
                img = cv.cvtColor(cv.imread('AlbumImages/im000'+str(i)+'.jpg'), cv.COLOR_BGR2GRAY)
            else:
                img = cv.cvtColor(cv.imread('AlbumImages/im00'+str(i)+'.jpg'), cv.COLOR_BGR2GRAY)

            ejes = AreaNucleo().coordenadaApertura(img, x, y) # y_Arri, y_Abaj, x_Izq, x_Der

            ejeY = ejes[0]
            ejeX = ejes[1]
            if self.nameButon == 'SSD':
                coordenadas = SSD().coordenadas(img, nucleo, ejes)
            elif self.nameButon == 'SAD':
                coordenadas = SAD().coordenadas(img, nucleo, ejes)
            elif self.nameButon == 'CC':
                coordenadas = CC().coordenadas(img, nucleo, ejes)
            print (i)
            print ( "Y: ", y, "\tNY: ",coordenadas[0], "\t\tRESTA: mvY:", y-coordenadas[0], "mvX:", x-coordenadas[1],"\n", "X: ", x, "\tNX: ", coordenadas[1], "\n\n" )

            imgAlineada = Alineacion().imgAlieada(img, coordenadas, y, x)

            Fondo = ((1 - gama) * Fondo) + (gama * imgAlineada)
            height, width = Fondo.shape
            size = (width,height)
            imgVideo.append(Fondo)
            cv.imwrite("Video/Video"+self.nameButon+"/Fondo_"+self.nameButon+str(i)+".jpg", Fondo)        
        cv.imwrite("Fondo_"+self.nameButon+".jpg", Fondo)
        self.grabarVideo()        
        self.ui.lblImgEspera.setPixmap(QPixmap("Fondo_"+self.nameButon+".jpg"))
        #fondo = QPixmap("Fondo_"+self.nameButon+".jpg")
        self.limpiarDatos()
        elapsed_time = time() - start_time
        print("Tiempo de ejecucion: ", elapsed_time)

    def grabarVideo(self):
        img_array = []
        for filename in glob.glob('Video/Video'+self.nameButon+'/*.jpg'):
            img = cv.imread(filename)
            height, width, layers = img.shape
            size = (width,height)
            img_array.append(img)

        out = cv.VideoWriter('Video'+self.nameButon+'.avi',cv.VideoWriter_fourcc(*'DIVX'), 15, size)

        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()

    def ecualizacion(self):
        imgEc = cv.imread ("Fondo_"+self.nameButon+".jpg" , 0)
        # crear un objeto CLAHE (los argumentos son opcionales).
        clahe = cv.createCLAHE (clipLimit = 3.0, tileGridSize = (40,40))
        cl1 = clahe.apply (imgEc)
        res = np.hstack((imgEc,cl1))
        cv.imwrite ('Fondo_CC_40_3.jpg' , res)
        imgEcualizada = cv.imread('Fondo_CC_40_3.jpg')
        cv.imshow("Ecualizada", imgEcualizada)

    def limpiarDatos(self):
        self.ui.editX.setText("")
        self.ui.editY.setText("")
        self.ui.editBeta.setText("")
        self.ui.editCantImg.setText("")

    def openVideo(self):
        cap = cv.VideoCapture('Video'+self.nameButon+'.avi')
        
        while True:
            ret, frame = cap.read()
            cv.imshow(self.nameButon, frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()

# ======================= MAIN ============================
app = QtWidgets.QApplication(sys.argv)
main = Principal()
main.show()
sys.exit(app.exec_())
