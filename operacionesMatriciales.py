import numpy as np

# Se define la primera matriz
matriz_1=[
    [8,4,2],
    [5,9,4],
    [3,14,7]
]

# Se define la segunda matriz
matriz_2=[
    [8,7,10],
    [8,9,8],
    [9,5,7]
]

# La funcion matmul efectua una multiplicacion
# entre las matrices especificadas como parametro
resultado=np.matmul(matriz_1,matriz_2)
print(resultado)
# [[114 102 126]
#  [148 136 150]
#  [199 182 191]]