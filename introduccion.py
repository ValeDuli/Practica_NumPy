#--------------------------------------------------------------#
#       NumPy: los conceptos básicos para principiantes        #
#--------------------------------------------------------------#

import numpy as np

a=np.array([[1,2,3],
            [4,5,6]])
print(a.shape)          # (2,3)

# La mayoría de las matrices NumPy tienen algunas restricciones. Por ejemplo:
#  - Todos los elementos de la matriz deben ser del mismo tipo de datos.
#  - Una vez creada, el tamaño total de la matriz no se puede cambiar.
#  - La forma debe ser “rectangular”, no “dentada”; por ejemplo, cada fila de 
#    una matriz bidimensional debe tener el mismo número de columnas.


#---------------------------------------#
#       Fundamentos de matrices         #
#---------------------------------------#

# Una forma de inicializar una matriz es mediante una secuencia de Python, como 
# una lista.
a=np.array([1,2,3,4,5,6])
print(a)                # [1 2 3 4 5 6]

# Podemos acceder a un elemento individual de esta matriz como lo haríamos con 
# un elemento de la lista original: utilizando el índice entero del elemento 
# entre corchetes.               
print(a[0])             # 1

# Al igual que la lista original, la matriz es mutable.
a[0]=10
print(a)                # [10 2 3 4 5 6]

# la notación de segmentos de Python se puede utilizar para indexar.
print(a[:3])            # [10 2 3]

# Una diferencia importante es que la indexación de una lista mediante segmentos 
# copia los elementos en una nueva lista, pero la segmentación de una matriz 
# devuelve una vista : un objeto que hace referencia a los datos de la matriz original. 
# La matriz original se puede modificar mediante la vista.
b=a[3:]
print(b)                # [4 5 6]
b[0]=40
print(a)                # [10 2 3 40 5 6]

# Se pueden inicializar matrices bidimensionales y de dimensiones superiores a partir de 
# secuencias anidadas de Python
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)                # [[ 1  2  3  4]
                        # [ 5  6  7  8]
                        # [ 9 10 11 12]]
# la dimensión de una matriz se la denomina a veces “eje”. Esta terminología puede resultar 
# útil para distinguir entre la dimensionalidad de una matriz y la dimensionalidad de los 
# datos representados por la matriz.
print(a[1,3])           # 8


#---------------------------------------#
#       Fundamentos de matrices         #
#---------------------------------------#

# El número de dimensiones de una matriz está contenido en el ndimatributo.
print(a.ndim)           # 2
# La forma de una matriz es una tupla de números enteros no negativos que 
# especifican la cantidad de elementos a lo largo de cada dimensión.
print(a.shape)          # (3, 4)
print(len(a.shape)==a.ndim) # True

# El número total fijo de elementos de la matriz está contenido en el size atributo.
print(a.size)           # 12
import math
print(a.size==math.prod(a.shape)) #True

# Las matrices suelen ser “homogéneas”. El tipo de datos se registra en el dtype atributo.
print(a.dtype)          # int64


#-----------------------------------------------------#
#       Agregar, eliminar y ordenar elementos         #
#-----------------------------------------------------#

# Ordenar una matriz es sencillo con np.sort(). Puedes especificar el eje, el tipo y el 
# orden cuando llamas a la función.
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(np.sort(arr)) #[1 2 3 4 5 6 7 8]
# Además de sort, que devuelve una copia ordenada de una matriz, puedes utilizar:
#  - argsort, que es una clasificación indirecta a lo largo de un eje especificado,
#  - lexsort, que es una ordenación estable indirecta sobre múltiples claves,
#  - searchsorted, que encontrará elementos en una matriz ordenada, y
#  - partition, que es una clasificación parcial.

# Puedes concatenarlos con np.concatenate()
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(np.concatenate((a, b)))   # [1 2 3 4 5 6 7 8]
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
print(np.concatenate((x, y), axis=0))   # [[1 2]
                                        # [3 4]
                                        # [5 6]]


#-------------------------------------------------------#
#       ¿Puedes cambiar la forma de una matriz?         #
#-------------------------------------------------------#

# El uso de arr.reshape()le dará una nueva forma a una matriz sin cambiar los datos. 
# Solo recuerde que cuando usa el método de remodelación, la matriz que desea producir debe 
# tener la misma cantidad de elementos que la matriz original. 
a = np.arange(6)
print(a)
b = a.reshape(3, 2)
print(b)
# Con np.reshape, puedes especificar algunos parámetros opcionales:
np.reshape(a, shape=(1, 6), order='C')


#-------------------------------------------------------#
#       ¿Cómo agregar un nuevo eje a una matriz?         #
#-------------------------------------------------------#

# Puede utilizar np.newaxisy np.expand_dimspara aumentar las dimensiones de su matriz existente.
# El uso np.newaxisaumentará las dimensiones de la matriz en una dimensión cuando se utilice una 
# vez. Esto significa que una matriz unidimensional se convertirá en una matriz bidimensional, 
# una matriz bidimensional se convertirá en una matriz tridimensional, y así sucesivamente.
a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)          # (6,)
a2 = a[np.newaxis, :]
print(a2.shape)         # (1, 6)
# Puede convertir explícitamente una matriz unidimensional en un vector de fila o de columna mediante 
# np.newaxis.
row_vector = a[np.newaxis, :]
print(row_vector.shape) # (1, 6)
print(row_vector)       # [[1 2 3 4 5 6]]
# O bien, para un vector de columna, puede insertar un eje a lo largo de la segunda dimensión
col_vector = a[:, np.newaxis]
print(col_vector.shape) # (6, 1)
print(col_vector)       # [[1]
                        # [2]
                        # [3]
                        # [4]
                        # [5]
                        # [6]]
