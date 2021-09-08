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

def reconstruir(matriz,solucion):
    fichas = []
    for elemento in solucion:
        if elemento == 0:
            try:
                fichas+=[[matriz[0][0],matriz[0][1]]]
                print("\n",fichas)
                
                #primero indice 1 luego indice 0, podria borrar indice 0 y luego 0 y daria lo mismo
                del matriz[0][1]
                del matriz[0][0]
                
                print("\n",matriz[0],"len: ",len(matriz[0]))
                for fila in matriz:
                    if(len(fila)==0):
                        print("\nentro a borrar fila: ",fila)
                        matriz.remove(fila)
                
            except IndexError:
                return False
        elif elemento == 1:
            try:
                fichas+=[[matriz[0][0],matriz[1][0]]]
                print("\naaa ",fichas)
                del matriz[0][0]
                del matriz[1][0]
                for fila in matriz:
                    if(len(fila)==0):
                        print("\naaa entro a borrar fila: ",fila)
                        matriz.remove(fila)
            except IndexError:
                return False
    return fichas

print(reconstruir([[1,1,1],[0,0,0]],[1,1,1]))


