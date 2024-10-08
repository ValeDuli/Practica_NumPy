#-------------------------------------------------------#
# ¿Cómo buscar el elemento máximo y mínimo en la matriz #
# dada usando NumPy?                                    #
#-------------------------------------------------------#
# La búsqueda es una técnica que ayuda a encontrar el 
# lugar de un elemento o valor determinado en la lista. 
# En Numpy, se pueden realizar varias operaciones de 
# búsqueda utilizando las distintas funciones que se 
# proporcionan en la biblioteca, como argmax , argmin , 
# etc.

import numpy as np
# Creamos un areglo de 5x4
array=np.arange(20).reshape(5,4)
print(array)
print()                             # [[ 0  1  2  3]
                                    # [ 4  5  6  7]
                                    # [ 8  9 10 11]
                                    # [12 13 14 15]
                                    # [16 17 18 19]]

# Si no se menciona ningún eje, entonces funciona en toda 
# la matriz.
print(np.argmax(array)) # 19

# Si axis = 1, entonces funciona en cada fila.
print(np.argmax(array, axis=1))     # [3 3 3 3 3]

# Si axis = 0, entonces funciona en cada columna.
print(np.argmax(array, axis=0))     # [4 4 4 4]

# De manera similar, se puede utilizar numpy.argmin( ) 
# para devolver los índices del elemento mínimo de la 
# matriz en un eje particular.
print(np.argmin(array)) # 0
print(np.argmin(array, axis=1))     # [0 0 0 0 0]
print(np.argmin(array, axis=0))     # [0 0 0 0]


#-------------------------------------------------------#
# ¿Cómo ordenar los elementos de la matriz dada usando  #
# Numpy?                                                #
#-------------------------------------------------------#
# Ordenar se refiere a organizar los datos en un formato 
# particular. El algoritmo de ordenación especifica la 
# forma de organizar los datos en un orden particular. 
# En Numpy, se pueden realizar varias operaciones de 
# ordenación utilizando las distintas funciones que se 
# proporcionan en la biblioteca, como sort , argsort, 
# etc.

array=np.array([
    [3,7,1],
    [10,3,2],
    [5,6,7]
])
print(array)
print()                             # [[ 3  7  1]
                                    # [10  3  2]
                                    # [ 5  6  7]]

# Ordenar toda la matriz
print(np.sort(array, axis=None))    # [ 1  2  3  3  5  6  7  7 10]

# Ordenar a lo largo de cada fila
print(np.sort(array, axis=1))       # [[ 1  3  7]
                                    # [ 2  3 10]
                                    # [ 5  6  7]]

# Ordenar a lo largo de cada columna
print(np.sort(array, axis=0))       # [[ 3  3  1]
                                    # [ 5  6  2]
                                    # [10  7  7]]
 
# Esta función devuelve los índices que ordenarían una matriz.                                   
array = np.array([28, 13, 45, 12, 4, 8, 0])
print(array)                        # [28 13 45 12  4  8  0]

print(np.argsort(array))            # [6 4 5 3 1 0 2]


#-------------------------------------------------------#
# ¿Cómo encontrar la media de cada matriz NumPy en la   #
# lista dada?                                           #
#-------------------------------------------------------#
# El enunciado del problema es una lista de matrices 
# NumPy, la tarea es encontrar la media de cada matriz 
# NumPy.

list = [
    np.array([3, 2, 8, 9]),
    np.array([4, 12, 34, 25, 78]),
    np.array([23, 12, 67])
]

result = []
for i in range(len(list)):
    result.append(float(np.mean(list[i])))
print(result)                       # [5.5, 30.6, 34.0]


#-------------------------------------------------------#
# ¿Cómo agregar filas y columnas en una matriz NumPy?   #
#-------------------------------------------------------#
# El enunciado del problema es una matriz NumPy, la 
# tarea es agregar filas/columnas según los requisitos 
# a la matriz NumPy.

# Agregar fila usando numpy.vstack()
array = np.array([
    [3, 2, 8],
    [4, 12, 34],
    [23, 12, 67]
])

newRow = np.array([2, 1, 8])
newArray = np.vstack((array, newRow))
print(newArray)                     # [[ 3  2  8]
                                    # [ 4 12 34]
                                    # [23 12 67]
                                    # [ 2  1  8]]
                                    
# Agregar una columna usando numpy.column_stack()
array = np.array([
    [3, 2, 8],
    [4, 12, 34],
    [23, 12, 67]
])

newColumn = np.array([2, 1, 8])
newArray = np.column_stack((array, newColumn))
print(newArray)                     # [[ 3  2  8  2]
                                    # [ 4 12 34  1]
                                    # [23 12 67  8]]


#-------------------------------------------------------#
#           ¿Cómo invertir una matriz NumPy?            #
#-------------------------------------------------------#
# El enunciado del problema es una matriz NumPy y la 
# tarea es invertir la matriz NumPy.
array = np.array([3, 6, 7, 2, 5, 1, 8])
reversedArray = np.flipud(array)
print(reversedArray)                # [8 1 5 2 7 6 3]


#-------------------------------------------------------#
# ¿Cómo multiplicar dos matrices en una sola línea      #
# usando NumPy?                                         #
#-------------------------------------------------------#
# El enunciado del problema se da con dos matrices y 
# hay que multiplicarlas en una sola línea usando NumPy.

matrix1 = [
    [3, 4, 2],
    [5, 1, 8],
    [3, 1, 9]
]

matrix2 = [
    [3, 7, 5],
    [2, 9, 8],
    [1, 5, 8]
]

result = np.dot(matrix1, matrix2)
print(result)                       # [[19 67 63]
                                    # [25 84 97]
                                    # [20 75 95]]


#-------------------------------------------------------#
# ¿Cómo imprimir el patrón de tablero de ajedrez de     #
# nxn usando NumPy?                                     #
#-------------------------------------------------------#
# Dado el enunciado del problema n, imprima el patrón 
# de tablero de ajedrez para una matriz nxn considerando 
# que 0 para negro y 1 para blanco.
n = 8

# Crea una matriz nxn llena de 0
matrix = np.zeros((n, n), dtype=int)

# llenar 1 con filas y columnas alternas
matrix[::2, 1::2] = 1
matrix[1::2, ::2] = 1

# Imprime el patrón de tablero de ajedrez
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()                         # 0 1 0 1 0 1 0 1
                                    # 1 0 1 0 1 0 1 0
                                    # 0 1 0 1 0 1 0 1
                                    # 1 0 1 0 1 0 1 0
                                    # 0 1 0 1 0 1 0 1
                                    # 1 0 1 0 1 0 1 0
                                    # 0 1 0 1 0 1 0 1
                                    # 1 0 1 0 1 0 1 0