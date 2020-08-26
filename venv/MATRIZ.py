import numpy as np
m = np.array([[4, 1, 23, 2, 3],
              [5, 2, 2, 7, 4],
              [9, 3, 12 , 8, 6],
              [2, 3, 12, 8, 6],
              [3, 4, 11, 1, 8]
              ])
print("elemtento de la fila 0 y columna 0 es: ", m[0, 0])
print("elemtento de la fila 1 y columna 2 es: ", m[1,2])
print("elemtento de la fila 3 y columna 4 es: ", m[3,4])
print("los elementod e la fila 0 son : ", m[0,::])
print("los elementod e la columna 0 son : ", m[::,0])
print("los elemento de la fila 1 hasta la 3 con columanas desde la 1 hasta la 2: ",  m[1:4,1:3])
print("diagonal principal rango: ", m[range(0, 5), range(0 ,5)])
print("diagonal secundaria rango: ", m[range(0, 5), range(4 ,-1, -1)])
print(np.arange(4, -1, -1))