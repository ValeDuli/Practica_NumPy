import numpy as np

arreglo=np.array([[1,3,5,7,15],[2,4,10,9,11],[8,6,14,13,12]])
print(arreglo)
print("--------------------")
# [[ 1  3  5  7 15]
# [ 2  4 10  9 11]
# [ 8  6 14 13 12]]

# Ordena el arreglo en su totalidad
print(np.sort(arreglo, axis=None))
print("--------------------")
# [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]

# Ordena los elementos de cada renglon
print(np.sort(arreglo, axis=1))
print("--------------------")
# [[ 1  3  5  7 15]
# [ 2  4  9 10 11]
# [ 6  8 12 13 14]]

# Ordena los elementos de cada columna
print(np.sort(arreglo, axis=0))
print("--------------------")
#[[ 1  3  5  7 11]
# [ 2  4 10  9 12]
# [ 8  6 14 13 15]]