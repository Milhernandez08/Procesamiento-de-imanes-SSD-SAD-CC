# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showIMG.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1334, 717)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1301, 501))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblImg = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lblImg.setObjectName("lblImg")
        self.horizontalLayout.addWidget(self.lblImg)
        self.lblImgEspera = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lblImgEspera.setObjectName("lblImgEspera")
        self.horizontalLayout.addWidget(self.lblImgEspera)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 520, 150, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblX = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblX.setObjectName("lblX")
        self.verticalLayout.addWidget(self.lblX)
        self.lblY = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblY.setObjectName("lblY")
        self.verticalLayout.addWidget(self.lblY)
        self.lblBeta = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblBeta.setObjectName("lblBeta")
        self.verticalLayout.addWidget(self.lblBeta)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(440, 520, 191, 128))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.editX = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.editX.setObjectName("editX")
        self.verticalLayout_2.addWidget(self.editX)
        self.editY = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.editY.setObjectName("editY")
        self.verticalLayout_2.addWidget(self.editY)
        self.editBeta = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.editBeta.setObjectName("editBeta")
        self.verticalLayout_2.addWidget(self.editBeta)
        self.editCantImg = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.editCantImg.setObjectName("editCantImg")
        self.verticalLayout_2.addWidget(self.editCantImg)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(660, 520, 160, 95))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnCoordenadas = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnCoordenadas.setObjectName("btnCoordenadas")
        self.verticalLayout_3.addWidget(self.btnCoordenadas)
        self.btnEcualizar = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnEcualizar.setObjectName("btnEcualizar")
        self.verticalLayout_3.addWidget(self.btnEcualizar)
        self.btnEjecutar = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnEjecutar.setObjectName("btnEjecutar")
        self.verticalLayout_3.addWidget(self.btnEjecutar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1334, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblImg.setText(_translate("MainWindow", "TextLabel"))
        self.lblImgEspera.setText(_translate("MainWindow", "TextLabel"))
        self.lblX.setText(_translate("MainWindow", "Posición en X"))
        self.lblY.setText(_translate("MainWindow", "Posición en Y"))
        self.lblBeta.setText(_translate("MainWindow", "Valor de Gama"))
        self.label.setText(_translate("MainWindow", "Cantidad de imagenes"))
        self.btnCoordenadas.setText(_translate("MainWindow", "Escoger Posición"))
        self.btnEcualizar.setText(_translate("MainWindow", "Ver Ecualización"))
        self.btnEjecutar.setText(_translate("MainWindow", "Ejecutar"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

