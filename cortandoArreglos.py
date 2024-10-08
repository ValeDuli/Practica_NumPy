import numpy as np

arreglo=np.array([2,4,6,8,10,12,14])

print(arreglo[1:4])
# Se especifica el rango de elementos. En este 
# caso devuelve los elementos marcados con los 
# indices 1, 2 y 3 (no se incluye el indice 4)
# [4 6 8] 

print(arreglo[::2])
# No hay indice inicial, asi que sera de 0
# No hay indice final, asi que abarcara todo el arreglo
# El salto es dos, asi que tomara valores alternados
# [2 6 10 14]