#Elaborado por : Gabriel Fallas y Mauricio Arrieta
#Fecha de creación: 07/09/2021 
#Última modificación: 27/09/2021
#Versión: 3.9.1

#Importación de librerias
import sys
import random
from PyQt5 import QtGui, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from funciones import *
from algoritmos import *
from time import *

#Definición de funciones
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("window.ui", self)
        self.setWindowTitle("Matriz de dominó")
        self.botonFB.clicked.connect(lambda:self.recibirMatriz(1))
        self.botonBacktracking.clicked.connect(lambda:self.recibirMatriz(2))
        self.show()

    def mostrarError(self, texto):
        """""
        Esta función muestra un mensaje de error cuando el usuario
        ingresa la matriz de forma incorrecta.
        """""
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Error")
        mensaje.setText(texto)
        mensaje.setIcon(QMessageBox.Critical) 
        mensaje.exec()

    def recibirMatriz(self, numBoton):
        """""
        Se recibe la matriz como un string, cada fila está separada por un 
        punto y coma. Se retorna una matriz para que pueda ser manejada.
        """""
        respuesta = convertirAMatriz(self.cajaMatriz.toPlainText())
        if isinstance(respuesta, str):
            self.mostrarError(respuesta)
        elif isinstance(respuesta, list):
            self.construirTabla(respuesta, numBoton)
        else:
            return self.mostrarAdvertencia("Ingrese datos válidos.")  

    def colorearCeldas(self, combinacion , matriz):
        """""
        Se colorean las celdas según su orientación en la solución.
        """""
        try:
            copiaMatriz = copy.deepcopy(matriz)
            indiceSolucion = 0
            posColumna = 0
            posFila = 0
            while posFila < len(copiaMatriz) and indiceSolucion < len(combinacion):
                r = random.randint(0, 220)
                g = random.randint(0, 220)
                b  = random.randint(0, 220)
                if posColumna == len(copiaMatriz[0]) :
                    posFila+=1
                    posColumna=0
                if copiaMatriz[posFila][posColumna] == -1:
                    posColumna+=1   
                    if posColumna == len(copiaMatriz[0]):
                        continue
                if combinacion[indiceSolucion] == 0 and copiaMatriz[posFila][posColumna] != -1:
                    copiaMatriz[posFila][posColumna] = -1
                    copiaMatriz[posFila][posColumna+1] = -1
                    self.tabla.item(posFila,posColumna).setBackground(QtGui.QColor(r,g,b))
                    self.tabla.item(posFila,posColumna+1).setBackground(QtGui.QColor(r,g,b))
                    posColumna+=2
                    indiceSolucion+=1
                elif combinacion[indiceSolucion] == 1 and copiaMatriz[posFila][posColumna] != -1:
                    copiaMatriz[posFila][posColumna] = -1
                    copiaMatriz[posFila+1][posColumna] = -1
                    self.tabla.item(posFila,posColumna).setBackground(QtGui.QColor(r,g,b))
                    self.tabla.item(posFila+1,posColumna).setBackground(QtGui.QColor(r,g,b))
                    posColumna+=1
                    indiceSolucion+=1                
            return ""
        except IndexError:
            return []             

    def construirTabla(self, matriz, numBoton):
        """""
        Esta función se encarga de construir la tabla dentro de la interfaz gráfica
        según el tamaño de la matriz junto a sus elementos.
        """""
        tiempoInicial = perf_counter()
        #Si es 1 fue que se presionó el botón de fuerza bruta.
        if numBoton == 1:
            combinaciones = bruteForce(matriz)
        #Si es 2 fue que se presionó el botón de backtracking.
        elif numBoton == 2:
            combinaciones = backtracking(matriz)
        tiempoFinal = perf_counter()
        duracion = tiempoFinal - tiempoInicial
        print(duracion)
        if isinstance(combinaciones, list):
            nFilas = len(matriz)
            nColumnas = len(matriz[0])
            self.tabla.setRowCount(nFilas)
            self.tabla.setColumnCount(nColumnas)
            posColumna = 0
            posFila = 0
            for i in matriz:
                for j in i:
                    self.tabla.setItem(posFila,posColumna, QTableWidgetItem(str(j)))
                    self.tabla.item(posFila,posColumna).setTextAlignment(Qt.AlignCenter)
                    self.tabla.item(posFila,posColumna).setForeground(QtGui.QColor(255,255,255))
                    posColumna += 1
                posColumna = 0
                posFila += 1
            self.colorearCeldas(combinaciones[0] ,matriz)
            self.lcdNumber.display(duracion)
        elif isinstance(combinaciones, str):
            self.mostrarError(combinaciones)
        else:
            return self.mostrarError("No se pudo realizar la operación.")
            
#Programa principal
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
