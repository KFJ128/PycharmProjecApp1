
#SUMA DE FILAS Y COLUMNAS
import numpy as np
def numerototal(filas, columnas):
    return np.random.randint(1, 10, (filas, columnas))
a = numerototal(5, 5)
vector_v = np.array([])
vector_w = np.array([])
print(a)
for v in range(0, 5):
    suma_filas = 0
    suma_columnas = 0
    cuadrado = 0
    cubica = 0
    vt = 0
    s = 0
    for w in range(0, 5):
        suma_filas += (a[v][w] ** 2)
        cuadrado = suma_filas ** 0.5
        suma_columnas += (a[w][v] ** 3)
        cubica = suma_columnas ** 0.3333
    print("filas: ", suma_filas)
    print("cuadrado: ", cuadrado)
    print("columnas: ", suma_columnas)
    print("cubica: ", cubica)
    print("diagonal principal: ", a[range(0, 5), range(0, 5)])
    print("diagonal secundaria: ", a[range(0, 5), range(4, -1, -1)])
    vector_v = np.insert(vector_v, v, cuadrado)
    vector_w = np.insert(vector_w, v, cubica)
vt = np.transpose([vector_v])
s = (1 / np.dot(vector_w, vt)) * (np.dot(vt, w))
print(s)






