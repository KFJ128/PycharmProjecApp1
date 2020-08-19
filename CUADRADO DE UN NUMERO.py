import numpy as np
numero = int(input(" leer valor a calcular: "))
valores = np.arange(1, 2 * numero, 2)
print("numero al cuadrado de", numero, "es:", np.sum(valores))


 #multiplicacion solo con sumas
import numpy as np
a = int(input(" leer primer valor A : "))
b = int(input(" leer primer valor B : "))
print(a, " * ", b, " = ", np.sum(np.zeros(b) + a))


#leer vector
n = int(input(" ingrese el tamaño del vector: "))
vector = np.arange(n)
for i in range(0, len(vector)):
    vector[i] = int(input("ingrese el elmento: "))
print(vector)

