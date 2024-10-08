import numpy as np

arreglo=np.array([[1,2,3,4,5],[6,7,8,9,10]])

# Cuando se usan arreglos multidimensionales, deben usarse
# ciclos anidados.
for i in arreglo:      # Recorre cada renglon de la matriz
    for j in i:        # Recorre las columnas del renglon
        print(j)
        # 1
        # 2
        # 3
        # 4
        # 5
        # 6
        # 7
        # 8
        # 9
        # 10