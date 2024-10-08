import numpy as np

np.random.seed(123) # Se especifica una semilla para generar valores aleatorios

matriz=np.random.randint(0,10,size=(7,7))
# Se especifica que matriz sera un arreglo de tamaño 7x7 (especificado con size)
# y que ademas estara relleno por valores al azar (generados con random)
# los cuales seran de tipo entero (randint) y estaran en un rango entre
# un limite inferior de 0 y un valor maximo de 9 (el limite superor es 10)

print(matriz)
# [[2 2 6 1 3 9 6]
#  [1 0 1 9 0 0 9]
#  [3 4 0 0 4 1 7]
#  [3 2 4 7 2 4 8]
#  [0 7 9 3 4 6 1]
#  [5 6 2 1 8 3 5]
#  [0 2 6 2 4 4 6]]