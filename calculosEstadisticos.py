import numpy as np

np.random.seed(123)
matriz=np.random.randint(0,10,size=(7,7))
print(matriz)

# Crearemos una lista que contenga el promedio de los elementos
# de cada renglon de la matriz que generamos en el ejemplo anterior
resultado=[]
for i in range(len(matriz)):                # El contador i recorre cada renglon de la matriz
    resultado.append(float(np.mean(matriz[i])))    # Se calcula el promedio del renglon i

print(resultado)
# [4.142857142857143, 2.857142857142857, 2.7142857142857144, 4.285714285714286, 
# 4.285714285714286, 4.285714285714286, 3.4285714285714284]

