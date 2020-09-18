#KEVIN FRANCISCO JIMÉNEZ BERMEO(2SO EJERCICIO.)
import numpy as np
def crearmatrizalealtoria(filas, columnas):
    return np.random.randint(1, 11, (filas, columnas))
matriz_a = crearmatrizalealtoria(10, 10)
print(matriz_a)
matriz_a_vt = np.zeros((10, 10))
for i in range(len(matriz_a)):
    for j in range(len(matriz_a)):
        matriz_a_vt[j, i] = matriz_a[i, j]
for k in range(len(matriz_a_vt)):
    matriz_a_vt[k, k] = 0
print(matriz_a_vt)
