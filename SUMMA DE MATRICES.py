
#suma de matriz + matriz
import numpy as np
A = np.random.randint(10, size=(5, 5))
B = np.random.randint(10, size=(5, 5))
C = np.empty((5, 5))
for i in range(len(A)):
    for j in range(len(A[i])):
        C[i, j] = A[i, j] + B[i, j]
print(A)
print(B)
print(C)



#suma
print("suma de filas - columnas: ")
import numpy as np
a = np.random.randint(10, size=(6, 6))
print(a)
cuadrado = 0
cubica = 0
for v in range(0, 6):
    sumafilas = 0
    sumacolumnas = 0
    for w in range(0, 6):
        sumafilas += (a[v][w]) ** 2
        cuadrado = (sumafilas ** 0.5)
        sumacolumnas += (a[w][v]) ** 3
        cubica = (sumacolumnas ** 0.33333333)
    print("\nLa suma de la fila " + str(v + 1) + " elevada al cuadrado es " + str(sumafilas))
    print("aplicando la formula de sumatoria con raiz cuadratica en cada fila su respuesta es: ", cuadrado)
    print("\nLa suma de la columna " + str(v + 1) + " elevada al cubo es " + str(sumacolumnas))
    print("aplicando la formula de sumatoria con raiz cubica en cada columna su respuesta es: ", cubica)









