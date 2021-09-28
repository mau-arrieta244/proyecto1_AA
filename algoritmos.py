#Elaborado por : Gabriel Fallas y Mauricio Arrieta
#Fecha de creación: 07/09/2021 
#Última modificación: 27/09/2021
#Versión: 3.9.1

#Importación de librerias
import itertools
import copy

#Definición de funciones
def combinaciones(n):
    #nos da una lista donde cada elemento es combinacion en formato string
    lista = [''.join(x) for x in itertools.product('01', repeat = n)]
    #nos da lista donde cada elemento es combinacion en formato integers dentro de listas
    listaSoluciones = []
    for elemento in lista:
        solucion = []
        while elemento != "":
            solucion+=[int(elemento[0])]
            elemento=elemento[1:]
        listaSoluciones+=[solucion]
    return listaSoluciones

def solucionSize(n):
    '''
    nos retorna el tamaño de las soluciones
    por ejemplo, para un juego doble 1, habran 3 posiciones en cada posible solucion
    solucionSize(1) = 3
    '''
    if n == 1:
        return 3
    return solucionSize(n-1)+(n+1)

def filaVisitada(lista):
    '''
    Le pasamos filas de la matriz, y nos retorna:
    True si ya todos sus elementos fueron visitados
    False si hay alguno que no ha sido visitado
    '''
    for elemento in lista:
        if elemento[1]==False:
            return False
    return True

def reconstruir(matriz,solucion):
    #primero, debemos meter la matriz en una estructura tipo [[3,false],[7,false]]
    #donde el booleano representa si este elemento ya fue tomado para armar una ficha
    nuevaMatriz = []
    for elemento in matriz:
        nuevaFila = []
        nuevaMatriz.append(nuevaFila)
        for valor in elemento:
            nuevaFila.append([valor,False])
    fichas = []
    indiceFila = 0
    indiceColumna = 0
    for elemento in solucion:
        if elemento == 0:
            try:
                if indiceColumna+1>=len(nuevaMatriz[0]) and nuevaMatriz[indiceFila][indiceColumna][1] == False:
                    return False
                #campos libres y no se sale out of bounds
                #elementos no han sido usados y existen
                elif (nuevaMatriz[indiceFila][indiceColumna][1] == False) and (nuevaMatriz[indiceFila][indiceColumna+1][1]==False):
                    fichas+=[[nuevaMatriz[indiceFila][indiceColumna][0],nuevaMatriz[indiceFila][indiceColumna+1][0]]]
                    #booleano a True (ya fueron utilizadas para armar una ficha)
                    nuevaMatriz[indiceFila][indiceColumna][1] = True
                    nuevaMatriz[indiceFila][indiceColumna+1][1] = True
                    #si con esta ficha termino la fila que hago?
                    if filaVisitada(nuevaMatriz[indiceFila]):
                        indiceFila+=1 #saltamos una fila abajo
                        indiceColumna = 0 #columna vuelve a ser 0
                    else:
                        indiceColumna+=2 #2 por que tomamos 2 elementos
                #donde estoy está libre pero siguiente ocupado
                #pasaria si hubiera un 1 en fila 0, luego bajo a fila 1 y ahi quiero poner un 0
                elif (nuevaMatriz[indiceFila][indiceColumna][1] == False) and (nuevaMatriz[indiceFila][indiceColumna+1][1]==True):
                    return False
                #donde estoy está ocupado
                #buscar campo libre por todas las columnas de la fila,
                #si no encontró, bajar de fila
                else:
                    while indiceFila<len(nuevaMatriz):
                        while indiceColumna < len(nuevaMatriz[0]):
                            #si donde estoy esta libre pero es ultimo elemento de la fila
                            if indiceColumna+1>=len(nuevaMatriz[0]) and nuevaMatriz[indiceFila][indiceColumna][1] == False:
                                return False
                            #donde estoy esta ocupado
                            elif nuevaMatriz[indiceFila][indiceColumna][1] == True:
                                #si con esta ficha termino la fila que hago?
                                if filaVisitada(nuevaMatriz[indiceFila]):
                                    indiceFila+=1 #saltamos una fila abajo
                                    indiceColumna = 0 #columna vuelve a ser 0
                                else:
                                    indiceColumna+=1 #2 por que tomamos 2 elementos                         
                            #campos libres y no se sale out of bounds
                            #elementos no han sido usados y existen
                            elif (nuevaMatriz[indiceFila][indiceColumna][1] == False) and (nuevaMatriz[indiceFila][indiceColumna+1][1]==False):
                                fichas+=[[nuevaMatriz[indiceFila][indiceColumna][0],nuevaMatriz[indiceFila][indiceColumna+1][0]]]
                                #booleano a True (ya fueron utilizadas para armar una ficha)
                                nuevaMatriz[indiceFila][indiceColumna][1] = True
                                nuevaMatriz[indiceFila][indiceColumna+1][1] = True
                                #si con esta ficha termino la fila que hago?
                                if filaVisitada(nuevaMatriz[indiceFila]):
                                    if(indiceFila+1>=len(nuevaMatriz)):
                                        return fichas
                                    else:
                                        indiceFila+=1 #saltamos una fila abajo
                                        indiceColumna = 0 #columna vuelve a ser 0                                    
                                else:
                                    indiceColumna+=2 #2 por que tomamos 2 elementos                                    
                            #donde estoy está libre pero siguiente ocupado
                            #pasaria si hubiera un 1 en fila 0, luego bajo a fila 1 y ahi quiero poner un 0
                            elif (nuevaMatriz[indiceFila][indiceColumna][1] == False) and (nuevaMatriz[indiceFila][indiceColumna+1][1]==True):
                                return False
                    return False   
            except IndexError:
                return False   
        #ficha orientacion vertical
        elif elemento == 1:
            if indiceFila+1>=len(nuevaMatriz):
                return False
            #si fila a la que llega esta llena
            elif filaVisitada(nuevaMatriz[indiceFila]):
                indiceFila+=1
            #si espacio no ha sido usado
            elif nuevaMatriz[indiceFila][indiceColumna][1] == False:
                fichas+=[[nuevaMatriz[indiceFila][indiceColumna][0],nuevaMatriz[indiceFila+1][indiceColumna][0]]]
                #booleano a True (ya fueron utilizadas para armar una ficha)
                nuevaMatriz[indiceFila][indiceColumna][1] = True
                nuevaMatriz[indiceFila+1][indiceColumna][1] = True
                #si con esta ficha termino la fila que hago?
                if filaVisitada(nuevaMatriz[indiceFila]):
                    indiceFila+=1 #saltamos una fila abajo
                    indiceColumna = 0 #columna vuelve a ser 0
                else:
                    indiceColumna+=1
            #espacio ya fue tomado (booleano en True)
            elif nuevaMatriz[indiceFila][indiceColumna][1] == True:
                #se terminó fila?
                if filaVisitada(nuevaMatriz[indiceFila]):
                    indiceFila+=1 #saltamos una fila abajo
                    indiceColumna = 0 #columna vuelve a ser 0
                    while indiceColumna<len(nuevaMatriz[0]):
                        if indiceFila+1>=len(nuevaMatriz):
                            return False
                        elif nuevaMatriz[indiceFila][indiceColumna][1] == False:
                            fichas+=[[nuevaMatriz[indiceFila][indiceColumna][0],nuevaMatriz[indiceFila+1][indiceColumna][0]]]
                            #booleano a True (ya fueron utilizadas para armar una ficha)
                            nuevaMatriz[indiceFila][indiceColumna][1] = True
                            nuevaMatriz[indiceFila+1][indiceColumna][1] = True
                            #si con esta ficha termino la fila que hago?
                            if filaVisitada(nuevaMatriz[indiceFila]):
                                indiceFila+=1 #saltamos una fila abajo
                                indiceColumna = 0 #columna vuelve a ser 0
                            else:
                                indiceColumna+=1
                        indiceColumna+=1
                else:
                    indiceColumna+=1
                    while indiceColumna<len(nuevaMatriz[0]):
                        if nuevaMatriz[indiceFila][indiceColumna][1] == False:
                            fichas+=[[nuevaMatriz[indiceFila][indiceColumna][0],nuevaMatriz[indiceFila+1][indiceColumna][0]]]
                            #booleano a True (ya fueron utilizadas para armar una ficha)
                            nuevaMatriz[indiceFila][indiceColumna][1] = True
                            nuevaMatriz[indiceFila+1][indiceColumna][1] = True
                            #si con esta ficha termino la fila que hago?
                            if filaVisitada(nuevaMatriz[indiceFila]):
                                indiceFila+=1 #saltamos una fila abajo
                                indiceColumna = 0 #columna vuelve a ser 0
                                break
                            else:
                                indiceColumna+=1
                                break         
                        indiceColumna+=1
            #checkear si con esa ficha se acaba fila    
    return fichas,solucion

def formarFichas(matriz, combinacion):
    '''
    Se encarga de forma las fichas de la matriz a partir de su
    orientación.
    '''
    try:
        copiaMatriz = copy.deepcopy(matriz)
        indiceSolucion = 0
        fichas = []
        posColumna = 0
        posFila = 0
        while posFila < len(copiaMatriz) and indiceSolucion < len(combinacion):
            ficha = []
            if posColumna == len(copiaMatriz[0]) :
                posFila+=1
                posColumna=0
            if copiaMatriz[posFila][posColumna] == -1:
                posColumna+=1   
                if posColumna == len(copiaMatriz[0]):
                    continue
            if combinacion[indiceSolucion] == 0 and copiaMatriz[posFila][posColumna] != -1:
                num1 = copiaMatriz[posFila][posColumna]
                num2 = copiaMatriz[posFila][posColumna+1]
                copiaMatriz[posFila][posColumna] = -1
                copiaMatriz[posFila][posColumna+1] = -1
                posColumna+=2
                ficha.append([num1, num2])
                fichas.append(ficha)
                indiceSolucion+=1
            elif combinacion[indiceSolucion] == 1 and copiaMatriz[posFila][posColumna] != -1:
                num1 = copiaMatriz[posFila][posColumna] 
                num2 = copiaMatriz[posFila+1][posColumna]
                copiaMatriz[posFila][posColumna] = -1
                copiaMatriz[posFila+1][posColumna] = -1
                posColumna+=1
                ficha.append([num1, num2])
                fichas.append(ficha)
                indiceSolucion+=1                
        return fichas
    except IndexError:
        return []                  

def determinarRepetidas(fichas):
    '''
    Determina si las fichas estan repetidas.
    '''
    if fichas != []:
        i = 0
        while i < len(fichas):
            ficha = fichas[i]
            j = 0
            while j < len(fichas):
                if j == i:
                    j+=1
                    continue
                if fichas[j] == ficha or [[fichas[j][0][1], fichas[j][0][0]]] == ficha:  
                    return True
                j+=1
            i+=1     
        return False 
    return True   

def bruteForce(matriz):
    #cuantos bits tendra cada solucion
    tamanoSolucion = solucionSize(len(matriz)-1)
    #nos da una lista donde cada elemento es combinacion en formato string
    lista = [''.join(x) for x in itertools.product('01', repeat = tamanoSolucion)]
    #nos da lista donde cada elemento es combinacion en formato integers dentro de listas
    #y cuando ha armado una combinacion , prueba reconstruir con esa antes de armar la siguiente
    listaSoluciones = []
    for elemento in lista:
        solucion = []
        while elemento != "":
            solucion+=[int(elemento[0])]
            elemento=elemento[1:]
        if reconstruir(matriz,solucion)!=False and determinarRepetidas(formarFichas(matriz, solucion)) == False:
            listaSoluciones+=[solucion]
    if listaSoluciones == []:
        return "No existen soluciones para la matriz dada." 
    else:
        return listaSoluciones
solucionesInvalidas = []

def reconstruirBacktrack(matriz,solucion,indiceMedio):
    #primero, debemos meter la matriz en una estructura tipo [[3,false],[7,false]]
    #donde el booleano representa si este elemento ya fue tomado para armar una ficha
    nuevaMatriz = []
    global solucionesInvalidas
    for elemento in matriz:
        nuevaFila = []
        nuevaMatriz.append(nuevaFila)
        for valor in elemento:
            nuevaFila.append([valor,False])
    fichas = []
    indiceFila = 0
    indiceColumna = 0
    for indice,elemento in enumerate(solucion):
        if elemento == 0:
            try:
                if indiceColumna+1>=len(nuevaMatriz[0]) and nuevaMatriz[indiceFila][indiceColumna][1] == False:
                    if(indice<=indiceMedio):
                        decimal = solucion[:indice+1]
                        if(decimal!=0 and decimal not in solucionesInvalidas  and decimal!=1):
                            solucionesInvalidas+=[decimal]
                    return False
                #campos libres y no se sale out of bounds
                #elementos no han sido usados y existen
                elif (nuevaMatriz[indiceFila][indiceColumna][1] == False) and (nuevaMatriz[indiceFila][indiceColumna+1][1]==False):
                    fichas+=[[nuevaMatriz[indiceFila][indiceColumna][0],nuevaMatriz[indiceFila][indiceColumna+1][0]]]
                    #booleano a True (ya fueron utilizadas para armar una ficha)
                    nuevaMatriz[indiceFila][indiceColumna][1] = True
                    nuevaMatriz[indiceFila][indiceColumna+1][1] = True
                    #si con esta ficha termino la fila que hago?
                    if filaVisitada(nuevaMatriz[indiceFila]):
                        indiceFila+=1 #saltamos una fila abajo
                        indiceColumna = 0 #columna vuelve a ser 0
                    else:
                        indiceColumna+=2 #2 por que tomamos 2 elementos
                #donde estoy está libre pero siguiente ocupado
                #pasaria si hubiera un 1 en fila 0, luego bajo a fila 1 y ahi quiero poner un 0
                elif (nuevaMatriz[indiceFila][indiceColumna][1] == False) and (nuevaMatriz[indiceFila][indiceColumna+1][1]==True):
                    if(indice<=indiceMedio):
                        decimal = solucion[:indice+1]
                        # decimal = listaBinariaADecimal(solucion[:indice+1])
                        if(decimal!=0 and decimal not in solucionesInvalidas and decimal!=1):
                            solucionesInvalidas+=[decimal]
                    return False
                #donde estoy está ocupado
                #buscar campo libre por todas las columnas de la fila,
                #si no encontró, bajar de fila
                else:
                    while indiceFila<len(nuevaMatriz):
                        while indiceColumna < len(nuevaMatriz[0]):
                            #si donde estoy esta libre pero es ultimo elemento de la fila
                            if indiceColumna+1>=len(nuevaMatriz[0]) and nuevaMatriz[indiceFila][indiceColumna][1] == False:
                                if(indice<=indiceMedio):
                                    #decimal = listaBinariaADecimal(solucion[:indice+1])
                                    decimal = solucion[:indice+1]
                                    if(decimal!=0 and decimal not in solucionesInvalidas and decimal!=1):
                                        solucionesInvalidas+=[decimal]
                                return False
                            #donde estoy esta ocupado
                            elif nuevaMatriz[indiceFila][indiceColumna][1] == True:
                                #si con esta ficha termino la fila que hago?
                                if filaVisitada(nuevaMatriz[indiceFila]):
                                    indiceFila+=1 #saltamos una fila abajo
                                    indiceColumna = 0 #columna vuelve a ser 0
                                else:
                                    indiceColumna+=1 #2 por que tomamos 2 elementos
                            #campos libres y no se sale out of bounds
                            #elementos no han sido usados y existen
                            elif (nuevaMatriz[indiceFila][indiceColumna][1] == False) and (nuevaMatriz[indiceFila][indiceColumna+1][1]==False):
                                fichas+=[[nuevaMatriz[indiceFila][indiceColumna][0],
                                nuevaMatriz[indiceFila][indiceColumna+1][0]]]
                                #booleano a True (ya fueron utilizadas para armar una ficha)
                                nuevaMatriz[indiceFila][indiceColumna][1] = True
                                nuevaMatriz[indiceFila][indiceColumna+1][1] = True
                                #si con esta ficha termino la fila que hago?
                                if filaVisitada(nuevaMatriz[indiceFila]):
                                    if(indiceFila+1>=len(nuevaMatriz)):
                                        return fichas
                                    else:
                                        indiceFila+=1 #saltamos una fila abajo
                                        indiceColumna = 0 #columna vuelve a ser 0
                                else:
                                    indiceColumna+=2 #2 por que tomamos 2 elementos
                            #donde estoy está libre pero siguiente ocupado
                            #pasaria si hubiera un 1 en fila 0, luego bajo a fila 1 y ahi quiero poner un 0
                            elif (nuevaMatriz[indiceFila][indiceColumna][1] == False) and (nuevaMatriz[indiceFila][indiceColumna+1][1]==True):
                                if(indice<=indiceMedio):
                                    decimal = solucion[:indice+1]
                                    if(decimal!=0 and decimal not in solucionesInvalidas and decimal!=1):
                                        solucionesInvalidas+=[decimal]
                                return False
                    if(indice<=indiceMedio):
                        decimal = solucion[:indice+1]
                        if(decimal!=0 and decimal not in solucionesInvalidas and decimal!=1):
                            solucionesInvalidas+=[decimal]
                    return False   
            except IndexError:
                if(indice<=indiceMedio):
                        decimal = solucion[:indice+1]
                        if(decimal!=0 and decimal not in solucionesInvalidas and decimal!=1):
                            solucionesInvalidas+=[decimal]
                return False
        #ficha orientacion vertical
        elif elemento == 1:
            if indiceFila+1>=len(nuevaMatriz):
                if(indice<=indiceMedio):
                        decimal = solucion[:indice+1]
                        if(decimal!=0 and decimal not in solucionesInvalidas and decimal!=1):
                            solucionesInvalidas+=[decimal]
                return False
            #si fila a la que llega esta llena
            elif filaVisitada(nuevaMatriz[indiceFila]):
                indiceFila+=1
            #si espacio no ha sido usado
            elif nuevaMatriz[indiceFila][indiceColumna][1] == False:
                fichas+=[[nuevaMatriz[indiceFila][indiceColumna][0],nuevaMatriz[indiceFila+1][indiceColumna][0]]]
                #booleano a True (ya fueron utilizadas para armar una ficha)
                nuevaMatriz[indiceFila][indiceColumna][1] = True
                nuevaMatriz[indiceFila+1][indiceColumna][1] = True
                #si con esta ficha termino la fila que hago?
                if filaVisitada(nuevaMatriz[indiceFila]):
                    indiceFila+=1 #saltamos una fila abajo
                    indiceColumna = 0 #columna vuelve a ser 0
                else:
                    indiceColumna+=1 
            #espacio ya fue tomado (booleano en True)
            elif nuevaMatriz[indiceFila][indiceColumna][1] == True:
                #se terminó fila?
                if filaVisitada(nuevaMatriz[indiceFila]):
                    indiceFila+=1 #saltamos una fila abajo
                    indiceColumna = 0 #columna vuelve a ser 0
                    while indiceColumna<len(nuevaMatriz[0]):
                        if indiceFila+1>=len(nuevaMatriz):
                            if(indice<=indiceMedio):
                                decimal = solucion[:indice+1]
                                if(decimal!=0 and decimal not in solucionesInvalidas and decimal!=1):
                                    solucionesInvalidas+=[decimal]
                            return False
                        elif nuevaMatriz[indiceFila][indiceColumna][1] == False:
                            fichas+=[[nuevaMatriz[indiceFila][indiceColumna][0],nuevaMatriz[indiceFila+1][indiceColumna][0]]]
                            #booleano a True (ya fueron utilizadas para armar una ficha)
                            nuevaMatriz[indiceFila][indiceColumna][1] = True
                            nuevaMatriz[indiceFila+1][indiceColumna][1] = True
                            #si con esta ficha termino la fila que hago?
                            if filaVisitada(nuevaMatriz[indiceFila]):
                                indiceFila+=1 #saltamos una fila abajo
                                indiceColumna = 0 #columna vuelve a ser 0
                            else:
                                indiceColumna+=1
                        indiceColumna+=1
                else:
                    indiceColumna+=1
                    while indiceColumna<len(nuevaMatriz[0]):
                        if nuevaMatriz[indiceFila][indiceColumna][1] == False:
                            fichas+=[[nuevaMatriz[indiceFila][indiceColumna][0],nuevaMatriz[indiceFila+1][indiceColumna][0]]]
                            #booleano a True (ya fueron utilizadas para armar una ficha)
                            nuevaMatriz[indiceFila][indiceColumna][1] = True
                            nuevaMatriz[indiceFila+1][indiceColumna][1] = True
                            #si con esta ficha termino la fila que hago?
                            if filaVisitada(nuevaMatriz[indiceFila]): 
                                indiceFila+=1 #saltamos una fila abajo
                                indiceColumna = 0 #columna vuelve a ser 0
                                break
                            else:
                                indiceColumna+=1
                                break
                        indiceColumna+=1                
    return fichas,solucion

def backtracking(matriz):
    tamanoSolucion = solucionSize(len(matriz)-1)
    #sera justo la mitad del arbol de soluciones
    indiceMedio = tamanoSolucion//2
    #nos da una lista donde cada elemento es combinacion en formato string
    lista = [''.join(x) for x in itertools.product('01', repeat = tamanoSolucion)]
    #nos da lista donde cada elemento es combinacion en formato integers dentro de listas
    listaSoluciones = []
    global solucionesInvalidas 
    for elemento in lista:
        solucion = []
        while elemento != "":
            solucion+=[int(elemento[0])]
            elemento=elemento[1:]
        #recorrido en loop desde segundo nivel hasta indiceMedio
        for indice in range(1,indiceMedio+1):
            if solucion[:indice] in solucionesInvalidas:
                pass
        else:
            sol = reconstruirBacktrack(matriz,solucion,indiceMedio)
            if sol!= False and determinarRepetidas(formarFichas(matriz, solucion)) == False:
                listaSoluciones+=[solucion]
    if listaSoluciones == []:
        return "No existen soluciones para la matriz dada." 
    else:
        return listaSoluciones

#============================================================================================================================
#================================================= PRUEBAS   ================================================================
#============================================================================================================================
#============================================================================================================================

#juego doble 1: (2**3 combinaciones)
#print(bruteForce([[1,0,1], [0,1,0]])) #no
#print(bruteForce([[1,1,1],[0,0,0]])) # ok
#print(backtracking([[1,1,1],[0,0,0]])) # ok

#juego doble 2: (2**6 combinaciones)
#print(bruteForce([[2,1,2,2], [0 ,1, 1, 2], [0,1,0,0]])) #  ok
#print(backtracking([[2,1,2,2], [0 ,1, 1, 2], [0,1,0,0]])) #  ok

#juego doble 3: (2**10 combinaciones)
#print(bruteForce([[2,2,2,3,3],[2,2,0,1,3],[1,3,0,1,1],[3,0,0,0,1]])) # ok
#print(backtracking([[2,2,2,3,3],[2,2,0,1,3],[1,3,0,1,1],[3,0,0,0,1]])) # ok

#juego doble 4: (2**15 combinaciones)
"""""
print(bruteForce([[1 ,2 ,4 ,0 ,4 ,3 ],
[0 ,3 ,3 ,4 ,4 ,2 ],
[1 ,1 ,3 ,4 ,1 ,0 ],
[0 ,1 ,0 ,3 ,4 ,2 ],
[0 ,2 ,3 ,1 ,2 ,2 ]])) #  ok

print(backtracking([[1 ,2 ,4 ,0 ,4 ,3 ],
[0 ,3 ,3 ,4 ,4 ,2 ],
[1 ,1 ,3 ,4 ,1 ,0 ],
[0 ,1 ,0 ,3 ,4 ,2 ],
[0 ,2 ,3 ,1 ,2 ,2 ]])) #  ok
"""""

#juego doble 5: (2**21 combinaciones)
"""""
print(backtracking(
[[5,5,5,3,3,4,4],
[2,4,1,0,5,2,4],
[1,0,0,2,1,2,5],
[2,4,2,1,3,3,0],
[3,3,3,4,5,0,0],
[5,2,1,1,1,4,0]])) #ok

print(bruteForce(
[[5,5,5,3,3,4,4],
[2,4,1,0,5,2,4],
[1,0,0,2,1,2,5],
[2,4,2,1,3,3,0],
[3,3,3,4,5,0,0],
[5,2,1,1,1,4,0]])) #ok
"""""
#juego doble 10
"""""
print(bruteForce([
[2, 7 ,7 ,3 ,6 ,8 ,7 ,7 ,0 ,5 ,8, 1] ,
[3 ,9 ,5 ,8 ,6 ,2 ,9 ,0 ,3 ,5 ,5 ,3] ,
[9 ,1 ,1 ,5 ,6 ,8 ,6 ,2 ,8 ,3 ,9 ,8 ],
[1 ,1 ,2 ,10 ,9 ,3 ,1 ,0 ,7 ,4 ,8 ,9],
[3 ,4 ,4 ,3 ,6 ,2 ,10 ,8 ,6 ,10 ,0 ,7] ,
[1 ,1 ,5 ,4 ,5 ,8 ,8 ,4 ,0 ,7 ,5, 5] , 
[1 ,6 ,10 ,4 ,3 ,10 ,8 ,6 ,4 ,2 ,10, 6] ,
[9 ,9 ,9 ,2 ,7 ,0 ,4, 4 ,8 ,3, 10, 10],
[2 ,2 ,1 ,2 ,6 ,0 ,9 ,0 ,1 ,6 ,5 ,5] ,
[2 ,0 ,7 ,0 ,7 ,0, 3, 3, 0, 1, 2, 6] ,
[10, 10 ,9 ,7 ,10 ,9 ,4 ,7 ,4 ,4 ,5 ,10 ]])) #profe, ocurre error de memoria
"""""
"""""
print(determinarRepetidas(formarFichas([
[2, 7 ,7 ,3 ,6 ,8 ,7 ,7 ,0 ,5 ,8, 1] ,
[3 ,9 ,5 ,8 ,6 ,2 ,9 ,0 ,3 ,5 ,5 ,3] ,
[9 ,1 ,1 ,5 ,6 ,8 ,6 ,2 ,8 ,3 ,9 ,8 ],
[1 ,1 ,2 ,10 ,9 ,3 ,1 ,0 ,7 ,4 ,8 ,9],
[3 ,4 ,4 ,3 ,6 ,2 ,10 ,8 ,6 ,10 ,0 ,7] ,
[1 ,1 ,5 ,4 ,5 ,8 ,8 ,4 ,0 ,7 ,5, 5] , 
[1 ,6 ,10 ,4 ,3 ,10 ,8 ,6 ,4 ,2 ,10, 6] ,
[9 ,9 ,9 ,2 ,7 ,0 ,4, 4 ,8 ,3, 10, 10],
[2 ,2 ,1 ,2 ,6 ,0 ,9 ,0 ,1 ,6 ,5 ,5] ,
[2 ,0 ,7 ,0 ,7 ,0, 3, 3, 0, 1, 2, 6] ,
[10, 10 ,9 ,7 ,10 ,9 ,4 ,7 ,4 ,4 ,5 ,10 ]], 
[0 ,0 ,0 ,0 ,1 ,1, 0 ,1 ,1 ,0 ,1 ,1 ,0 ,1 ,1 ,0 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1, 1 ,0 ,0, 1, 1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1, 0, 0 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,0 ,1, 1, 0 ,0 ,0 ,0])))
"""""

