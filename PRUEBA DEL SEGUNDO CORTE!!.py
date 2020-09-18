#KEVIN FRANCISCO JIMÉNEZ BERMEO(2SO EJERCICIO.)
import numpy as np
def crearmatrizalealtoria(filas, columnas):
    return np.random.randint(1, 11, (filas, columnas))
matriz_a = crearmatrizalealtoria(10, 10)
print(matriz_a)