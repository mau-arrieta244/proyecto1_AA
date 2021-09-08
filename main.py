#Elaborado por : Gabriel Fallas y Mauricio Arrieta
#Fecha de creación: 07/09/2021 
#Última modificación:
#Versión: 3.9.1

#Importación de librerias
from funciones import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit
from PyQt5 import uic

#Programa principal
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("window.ui", self)
        self.setWindowTitle("Matriz de dominó")
        #self.botonFB.clicked.connect(self.printHola)
        self.show()
    """""
    def printHola(self):
        nombre = self.cajaMatriz.toPlainText()
        print(nombre)
    """""
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
