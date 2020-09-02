#suma
print("suma de filas - columnas: ")
import numpy as np
a = np.array([[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8], [7, 8, 9, 10]])
v1 = np.array([])
w1 = np.array([])
print(a)
cuadrado = 0
cubica = 0
for v in range(0, 4):
    sumafilas = 0
    sumacolumnas = 0
    for w in range(0, 4):
        sumafilas += (a[v][w]) ** 2
        cuadrado = (sumafilas ** 0.5)
        sumacolumnas += (a[w][v]) ** 3
        cubica = (sumacolumnas ** 0.33333333)
    print("\nLa suma de la fila " + str(v + 1) + " elevada al cuadrado es " + str(sumafilas))
    print("aplicando la formula de sumatoria con raiz cuadratica en cada fila su respuesta es: ", cuadrado)
    print("\nLa suma de la columna " + str(v + 1) + " elevada al cubo es " + str(sumacolumnas))
    print("aplicando la formula de sumatoria con raiz cubica en cada columna su respuesta es: ", cubica)
    v1 = np.insert(v1, v, cuadrado)
    w1 = np.insert(w1, v, cubica)


matriz = np.array([v1, w1])
matriz2=np.transpose(matriz)
print (matriz2)
s=(1/(w*np.transpose(v1))) * (np.transpose(v1)*w)
print(s)


