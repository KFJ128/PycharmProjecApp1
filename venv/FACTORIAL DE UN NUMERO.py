import numpy as np
n = int(input(" valor a factorizar: "))
vector = np.arange(2, n+1)
print(vector)
print("el factorial de: ", n , "!=", np.prod(vector))


#formual de leibniz
import numpy as np
suma_pi = 0
pi = np.arange(0, 1000)
suma_pi += np.sum(((-1)**pi) / (2*pi+1))
print(f"{suma_pi*4}")


import numpy as np

lim = int(input("Ingrese limite: "))
suma = 0
leibniz = np.arange(0, lim)
suma += np.sum(((-1)**leibniz) / (2*leibniz+1))
print(suma  * 4)



