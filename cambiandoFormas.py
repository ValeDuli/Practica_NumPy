import numpy as np

arreglo=np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(arreglo.shape)
# La instruccion shape nos devolvera, en este caso un 
# valor de (2,5), lo que significa que el arreglo tiene 
# dos dimensiones, com 2 renglones y 5 columnas
# (2, 5)

#------------------------------------------------------#
arreglo=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

arreglo_2=arreglo.reshape(3,5)
# Se almacena en una nueva variable un arreglo bidimensional con 
# 3 renglones y 5 columnas, usando los mismos elementos del 
# arreglo original.

print(arreglo_2)
# Despliega el contenido del nuevo arreglo
#[[ 1  2  3  4  5]
# [ 6  7  8  9 10]
# [11 12 13 14 15]]