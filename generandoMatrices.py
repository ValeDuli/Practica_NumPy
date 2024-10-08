import numpy as np

matriz=np.full((4,4),75)
# General una matriz de 4x4 y la llena 
# con el numero 75

print(matriz)
# Despliega la matriz
#[[75 75 75 75]
# [75 75 75 75]
# [75 75 75 75]
# [75 75 75 75]]

# Esta es una forma alternativa
# de lograr el mismo resultado

# Genera una matriz de 4x4 rellena 
# con el numero 1
matriz=np.ones((4,4))

# Multiplica el contenido de la
# matriz por el numero 75
matriz=75*matriz

print(matriz)
#[[75. 75. 75. 75.]
# [75. 75. 75. 75.]
# [75. 75. 75. 75.]
# [75. 75. 75. 75.]]
