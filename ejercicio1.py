import numpy as np

n=10

matrix=np.full((10,10),6)
# [[6 6 6 6 6 6 6 6 6 6]
#  [6 6 6 6 6 6 6 6 6 6]
#  [6 6 6 6 6 6 6 6 6 6]
#  [6 6 6 6 6 6 6 6 6 6]
#  [6 6 6 6 6 6 6 6 6 6]
#  [6 6 6 6 6 6 6 6 6 6]
#  [6 6 6 6 6 6 6 6 6 6]
#  [6 6 6 6 6 6 6 6 6 6]
#  [6 6 6 6 6 6 6 6 6 6]
#  [6 6 6 6 6 6 6 6 6 6]]

matrix[::2,1::2]=9
# [[6 9 6 9 6 9 6 9 6 9]
#  [6 6 6 6 6 6 6 6 6 6]
#  [6 9 6 9 6 9 6 9 6 9]
#  [6 6 6 6 6 6 6 6 6 6]
#  [6 9 6 9 6 9 6 9 6 9]
#  [6 6 6 6 6 6 6 6 6 6]
#  [6 9 6 9 6 9 6 9 6 9]
#  [6 6 6 6 6 6 6 6 6 6]
#  [6 9 6 9 6 9 6 9 6 9]
#  [6 6 6 6 6 6 6 6 6 6]]

matrix[1::2,::2]=9
# [[6 9 6 9 6 9 6 9 6 9]
#  [9 6 9 6 9 6 9 6 9 6]
#  [6 9 6 9 6 9 6 9 6 9]
#  [9 6 9 6 9 6 9 6 9 6]
#  [6 9 6 9 6 9 6 9 6 9]
#  [9 6 9 6 9 6 9 6 9 6]
#  [6 9 6 9 6 9 6 9 6 9]
#  [9 6 9 6 9 6 9 6 9 6]
#  [6 9 6 9 6 9 6 9 6 9]
#  [9 6 9 6 9 6 9 6 9 6]]

for i in range(n):
    for j in range (n):
        print(matrix[i][j], end=" ")
    print()
    # 6 9 6 9 6 9 6 9 6 9 
    # 9 6 9 6 9 6 9 6 9 6 
    # 6 9 6 9 6 9 6 9 6 9 
    # 9 6 9 6 9 6 9 6 9 6 
    # 6 9 6 9 6 9 6 9 6 9 
    # 9 6 9 6 9 6 9 6 9 6 
    # 6 9 6 9 6 9 6 9 6 9 
    # 9 6 9 6 9 6 9 6 9 6 
    # 6 9 6 9 6 9 6 9 6 9 
    # 9 6 9 6 9 6 9 6 9 6