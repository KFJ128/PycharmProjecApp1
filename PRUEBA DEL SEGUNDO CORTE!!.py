#KEVIN FRANCISCO JIMÉNEZ BERMEO(2SO EJERCICIO.)
import numpy as np
def crearmatrizalealtoria(filas, columnas):
    return np.random.randint(1, 11, (filas, columnas))
matriz_a = crearmatrizalealtoria(10, 10)
print(matriz_a)
matriz_a_vt = np.zeros((10, 1))
for j in range(1, matriz_a[range(0, 10), range(0, 10)]):
    for i in range(len(matriz_a)):
        matriz_a_vt[i, 0] = matriz_a[0, i]
    print(matriz_a_vt)

