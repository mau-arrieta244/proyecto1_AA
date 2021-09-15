#tests matrices



def combinaciones(n,lista,i):
    
    if(i==n):
        print("\n",lista)
        return
    else:
        lista[i]=0
        combinaciones(n,lista,i+1)

        lista[i]=1
        combinaciones(n,lista,i+1)    
        


#combinaciones(6,6*[0],0)

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
    #print(nuevaMatriz)
    
    fichas = []
    indiceFila = 0
    indiceColumna = 0

    for elemento in solucion:
        
        if elemento == 0:
            if indiceColumna+1>=len(nuevaMatriz[0]) and nuevaMatriz[indiceFila][indiceColumna][1] == False:
                print("\ncolumna: ",indiceColumna," fila: ",indiceFila)
                print("false 1, out of bounds derecha")
                return False
            
            #campos libres y no se sale out of bounds
            #elementos no han sido usados y existen
            elif (nuevaMatriz[indiceFila][indiceColumna][1] == False) and (nuevaMatriz[indiceFila][indiceColumna+1][1]==False):
                fichas+=[[nuevaMatriz[indiceFila][indiceColumna][0],nuevaMatriz[indiceFila][indiceColumna+1][0]]]
                print("\n acabo de meter ficha(s): ",fichas)
                #booleano a True (ya fueron utilizadas para armar una ficha)
                nuevaMatriz[indiceFila][indiceColumna][1] = True
                nuevaMatriz[indiceFila][indiceColumna+1][1] = True
                #si con esta ficha termino la fila que hago?
                if filaVisitada(nuevaMatriz[indiceFila]):
                    
                    indiceFila+=1 #saltamos una fila abajo
                    indiceColumna = 0 #columna vuelve a ser 0
                    print("\n termine fila, sigo con fila:",indiceFila," y columna: ",indiceColumna)
                    
                else:
                    indiceColumna+=2 #2 por que tomamos 2 elementos
                    print("\n tomé dos elementos, indice  = ",indiceColumna)
                    
            #donde estoy está libre pero siguiente ocupado
            #pasaria si hubiera un 1 en fila 0, luego bajo a fila 1 y ahi quiero poner un 0
            elif (nuevaMatriz[indiceFila][indiceColumna][1] == False) and (nuevaMatriz[indiceFila][indiceColumna+1][1]==True):
                print("false 2, espacio libre pero alapar ocupado")
                return False

            #donde estoy está ocupado
            #buscar campo libre por todas las columnas de la fila,
            #si no encontró, bajar de fila
            else:
                while indiceFila<len(nuevaMatriz):
                    while indiceColumna < len(nuevaMatriz[0]):
                        print("\n , " ,indiceColumna," fila:",indiceFila)

                        #si donde estoy esta libre pero es ultimo elemento de la fila
                        if indiceColumna+1>=len(nuevaMatriz[0]) and nuevaMatriz[indiceFila][indiceColumna][1] == False:
                            print("false 4, outofbounds derecha en ciclo")
                            return False
                        #donde estoy esta ocupado
                        elif nuevaMatriz[indiceFila][indiceColumna][1] == True:
                            print("entre aqui!")
                            #si con esta ficha termino la fila que hago?
                            if filaVisitada(nuevaMatriz[indiceFila]):
                                indiceFila+=1 #saltamos una fila abajo
                                indiceColumna = 0 #columna vuelve a ser 0
                                
                            else:
                                print("jeje bugs")
                                print("indice columna: ",indiceColumna)
                                indiceColumna+=1 #2 por que tomamos 2 elementos
                                print("indice columna: ",indiceColumna)
                            
            
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
                            print("false 2, espacio libre pero alapar ocupado")
                            return False
                        
                        
                    

                print("false ? no encontro campo libre en ninguna parte")
                return False      

                
                
                    



            
        #ficha orientacion vertical
        elif elemento == 1:
            
            if indiceFila+1>=len(nuevaMatriz):
                print("\njeje out of bounds abajo",fichas)
                return False
            #si espacio no ha sido usado
            elif nuevaMatriz[indiceFila][indiceColumna][1] == False:
                print("aca>")
                fichas+=[[nuevaMatriz[indiceFila][indiceColumna][0],nuevaMatriz[indiceFila+1][indiceColumna][0]]]
                #booleano a True (ya fueron utilizadas para armar una ficha)
                nuevaMatriz[indiceFila][indiceColumna][1] = True
                nuevaMatriz[indiceFila+1][indiceColumna][1] = True
                print("fichas: ",fichas)
                #si con esta ficha termino la fila que hago?
                if filaVisitada(nuevaMatriz[indiceFila]):
                    print("random ass shit!")
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
                        if nuevaMatriz[indiceFila][indiceColumna][1] == False:
                            fichas+=[[nuevaMatriz[indiceFila][indiceColumna][0],nuevaMatriz[indiceFila+1][indiceColumna][0]]]
                            print("fichas2: ",fichas)
                            #booleano a True (ya fueron utilizadas para armar una ficha)
                            
                            nuevaMatriz[indiceFila][indiceColumna][1] = True
                            
                            nuevaMatriz[indiceFila+1][indiceColumna][1] = True
                            
                            #si con esta ficha termino la fila que hago?
                            if filaVisitada(nuevaMatriz[indiceFila]):
                                indiceFila+=1 #saltamos una fila abajo
                                indiceColumna = 0 #columna vuelve a ser 0
                                
                            
                            else:
                                print("else else")
                                indiceColumna+=1
                            
                        indiceColumna+=1
                else:
                    indiceColumna+=1
                    while indiceColumna<len(nuevaMatriz[0]):
                        if nuevaMatriz[indiceFila][indiceColumna][1] == False:
                            fichas+=[[nuevaMatriz[indiceFila][indiceColumna][0],nuevaMatriz[indiceFila+1][indiceColumna][0]]]
                            print("fichas56: ",fichas)
                            #booleano a True (ya fueron utilizadas para armar una ficha)
                            nuevaMatriz[indiceFila][indiceColumna][1] = True
                            print("caida imperioromano")
                            nuevaMatriz[indiceFila+1][indiceColumna][1] = True
                            #si con esta ficha termino la fila que hago?
                            if filaVisitada(nuevaMatriz[indiceFila]):
                                print("huh?")
                                indiceFila+=1 #saltamos una fila abajo
                                indiceColumna = 0 #columna vuelve a ser 0
                                break
                            
                            else:
                                print("huh 222?")
                                indiceColumna+=1
                                break
                            
                        indiceColumna+=1
                
                
                    

                

            #checkear si con esa ficha se acaba fila

                
    return fichas


#combinaciones(3,3*[0],0)

print(reconstruir([[0,4,0,3,1,0],[0,3,1,2,1,3],[4,4,0,1,4,3],[4,2,2,1,2,0],[4,1,3,3,2,2]],[1,0,1,1,1,0,0,0,0,0,0,0,0,0,0]))








