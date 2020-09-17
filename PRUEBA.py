##suma de filas y de columnas
import numpy as np
def numero_filas_columnas (filas, columnas):
    return np.random.randint(0, 11, (filas, columnas))
matriz = numero_filas_columnas(5, 5)
print(matriz)
v1 = np.array([])
w1 = np.array([])
vt = np.array([])
for v in range(0, 5):
    suma_filas = 0
    cuadrado = 0
    suma_columnas = 0
    cubo = 0
    for w in range(0, 5):
        suma_filas += (matriz[v][w]) ** 2
        cuadrado = suma_filas ** 0.5
        suma_columnas += (matriz[w][v]) ** 3
        cubo = suma_columnas ** 0.33333
    print("suma de fila", str(v + 0), "es = ", suma_filas)
    print(cuadrado)
    print("suma de columna", str(v + 0), "es = ", suma_columnas)
    print(cubo)
    v1 = np.insert(v1, v, cuadrado)
    w1 = np.insert(w1, v,  cubo)
    vt = np.transpose(v1)
print(v1)
print(w1)
vt = np.array([v1])


#multipliacion de matrices
import numpy as np
def matriz1(filas, columnas):
    return np.random.randint(0, 11, (filas, columnas))
matrizaa = matriz1(4, 4)
print(matrizaa)
def matriz2(fila, columna):
    return np.random.randint(0, 11, (fila, columna))
matrizbb = matriz2(4, 4)
matrizc = np.zeros((4, 4))
print(matrizbb)
for i in range(len(matrizaa)):
    for j in range(len(matrizaa[i])):
        matrizc[i, j] = matrizaa[i, j] * matrizbb[i, j]
print(matrizc)
print(matrizaa * matrizbb)


#decimal a binario
numero = int(input(" leer el valor a convertir a binario: "))
lista = []
while numero >= 1:
    lista.append(str(numero % 2))
    numero //= 2
print("".join(lista[::-1]))


#Realizar un algoritmo que calcule el valor aproximada de pi, basa en el método Euler:Realizar un algoritmo que calcule el valor aproximada de pi, basa en el método Euler:
e = int(input(" leer el valor: "))
resultado = 0
f1 = 1
f2 = 1
n1 = 0
n2 = 0
for m in range(0, e):
    e = m
    n1 = e
    n2 = (2 * e) + 1
    for i in range(1, n1 + 1):
        f1 *= i
    for j in range(1, n2 + 1):
        f2 *= j
    resultado += (2 ** e) * (f1 ** 2) / f2
    f1 = 1
    f2 = 1
print(resultado)

#numero base_exponente
base = int(input(" leer la base: "))
exponente = int(input(" leer el exponente: "))
resultado = base
t = 0
for i in range(1, exponente):   
    for j in range(1, base + 1):
        t += resultado
    resultado = t
    t = 0
print(resultado)









