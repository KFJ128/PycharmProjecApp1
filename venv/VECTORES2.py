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





#binario a decimal
import numpy as np
entrada = input("ingrese el número binario: ")
cadena = entrada[::1]
salida = 0; expo = 0
while expo < len(cadena):
    if (int(cadena[expo]) == 1):
        salida += int(cadena[expo]) * 2 ** expo
    expo += 1
print(" el resultado es: ", salida)
# a octal es
num= salida
vec = []
while num >= 1:
    vec.append(str(num % 8))
    num //= 8
print("octal es:", "".join(vec[::-1]))
# a hexadecimal es
numero = int(salida)
vec_hex = []
while numero >= 1:
    resto = numero % 16
    if resto >= 10:
        if resto == 10:
            vec_hex.append("A")
        elif resto == 11:
            vec_hex.append("B")
        elif resto == 12:
            vec_hex.append("C")
        elif resto == 13:
            vec_hex.append("D")
        elif resto == 14:
            vec_hex.append("E")
        else:
            vec_hex.append("F")
    else:
        vec_hex.append(resto)
    numero //= 16
vec_hex.reverse()

print("hexadecimal es: ", vec_hex)




#decimal a binario
num = float(input(" ingresar valor decimal a binario : "))
lista = []
while num >= 1:
    lista.append(str (num % 2))
    num //= 2
print( "".join(lista[::-1]))



#decimal a octal
num= float(input(" ingrese el número decimal a octal: "))
vec = []
while num >= 1:
    vec.append(str(num % 8))
    num //= 8
print("".join(vec[::-1]))



#decimal a hexadecimal
num= float(input(" ingrese el número decimal a hexadecimal: "))
vec = []
while num >= 1:
    vec.append(str(num % 16))
    num //= 16
print("".join(vec[::-1]))





#decimal a hexadecimal
num= float(input(" ingrese el número decimal a hexadecimal: "))
vec_hex = []
while numero >= 1:
    residuo = numero % 16
    if residuo >= 10:
        if residuo == 10:
            vec_hex.append(str("A"))
        elif residuo == 11:
            vec_hex.append(str("B"))
        elif residuo == 12:
            vec_hex.append(str("C"))
        elif residuo == 13:
            vec_hex.append(str("D"))
        elif residuo == 14:
            vec_hex.append(str("E"))
        else:
            vec_hex.append(str("F"))
    else:
        vec_hex.append(str(residuo))
    numero //= 16
vec_hex.reverse()

print("hexadecimal es: ", vec_hex)






