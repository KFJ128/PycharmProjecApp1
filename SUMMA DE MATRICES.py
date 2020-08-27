
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
for i in range(0, 6):
 sumafilas = 0
 sumacolumnas = 0
 for j in range(0, 6):
        sumafilas += (a[i][j]) ** 2
        cuadrado = (sumafilas ** 0.5)
        sumacolumnas += (a[j][i]) ** 3
        cubica = (sumafilas ** 0.33333333)
 print("\nLa suma de la fila elevada al cuadrado " + str(i + 1) + " es " + str(sumafilas))
 print("aplicando la formula de sumatoria con raiz cuadratica en cada fila su respuesta es: ", cuadrado)
 print("\nLa suma de la columna elevada al cubo " + str(i + 1) + " es " + str(sumacolumnas))
 print("aplicando la formula de sumatoria con raiz cubica en cada columna su respuesta es: ", cubica)









