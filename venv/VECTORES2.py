import numpy as np
v = np.array([10, 2, 9, 9, 7, 10, 5, 2, 3, 7]) #creando un vector
print(v)
print(len(v))
print("el primer elemento es: ", v[0])
print("el ultimo elemento es: ", v[9])
print(" los valores del rango 2 al 4: ", v[2:5] )# acceder al ultimom rango de valore



#hallar la cedula
import numpy as np
cedula = np.array([1, 7, 2, 7, 6, 6, 6, 8, 3]) #vector cedula
print(cedula)
print("los valores de las posiciones impares son: ", cedula[1:8:2])
sumaimpar = np.sum(cedula[1:8:2]) # suma los elementos o los digitos de las porsiciones impares
print("sumatoria impar:", sumaimpar)

print("los valores de las posiciones pares son: ", cedula[0:9:2])
pares = cedula[0:9:2] * 2
print(pares)
for i in range(0, len(pares)): #recorrer el vector con contadores de posicion
    if pares[i] > 9:
        pares[i] -= 9
print(" nuevos valores son: ", pares)
sumapar = np.sum(pares)
print("suma de pares: ", sumapar)
sumatotal = sumaimpar + sumapar
udg = sumatotal % 10 - 10
print("ultimo digito de la cedula es: ", udg)






