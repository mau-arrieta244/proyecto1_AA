#Elaborado por : Gabriel Fallas y Mauricio Arrieta
#Fecha de creación: 07/09/2021 
#Última modificación:
#Versión: 3.9.1

#Importación de librerias

#Definición de funciones
def convertirAMatriz(string):
    """""
    Función: recibe el string de la GUI y lo convierte en matriz.
    Entradas: el string de la GUI.
    Salidas: la matriz creada.
    """""
    matriz = []
    subMatriz = []
    if string != "":
        if string[-1] == ";":
            if len(string) >= 8:
                for i in string:
                    if i != ";":
                        if i != " ":
                            try:
                                intI = int(i)
                                subMatriz.append(intI)    
                            except:
                                return "No se pueden insertar letras, solo números."
                    else:
                        if len(matriz) > 0 and len(subMatriz) != len(matriz[0]):
                            return "Cada fila debe tener la misma longitud."
                        else:
                            matriz.append(subMatriz)
                            subMatriz = []      
                return matriz
            return "Las dimensiones mínimas de la matriz son de 2 x 3."     
        return "Debe finalizar cada fila con un punto y coma."         
    return "Coloque una matriz en el espacio en blanco."

#Programa principal
"""""
print(convertirAMatriz("1 1 1; 0 0 0;"))
print(convertirAMatriz("111;000;"))
print(convertirAMatriz("a 2 3; 4 5 6;"))
print(convertirAMatriz("1 2 3; 4 5;"))
print(convertirAMatriz(";"))
print(convertirAMatriz("aaa;aaa;"))
print(convertirAMatriz("2 1 2 2 ;0 1 1 2;0 1 0 0;"))
print(convertirAMatriz("2122;0112;0100;")) 
print(determinarDimensiones(convertirAMatriz("1 1 1; 0 0 0;")))
print(determinarDimensiones(convertirAMatriz("2 1 2 2; 0 1 1 2; 0 1 0 0;")))
print(determinarDimensiones(convertirAMatriz("2 3 3 2 2 ; 3 0 3 0 2 ; 2 1 3 1 0 ;1 0 1 1 0 ;")))
"""""