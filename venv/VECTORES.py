





vector1 = []
n = int(input(" leer el limite: "))
for i in range(0, n):
    vector1.append(int(input(" escribir valores del vector: ")))
print(" el vector tiene: ", len(vector1), " elementos ")
for j in range(0, len(vector1)):
    print(" elemento del vector ", j,":",  vector1[j])




#algoritmo pirmo o compuesto
numero = int(input(" leer valor del número:"))
numero2 = int(numero)
numero_cuadrado = int(numero2 // (numero) ** (1 / 2))
print("piso del numero: ", numero_cuadrado)
for d in range(1, numero_cuadrado+1):
    if  numero_cuadrado % d == 1:
      print(" rango de numero compuesto de", numero_cuadrado, " % ", d, " es igual a: ",  numero_cuadrado % d)
    else:
     print(" rango de numero primos de", numero_cuadrado, " % ", d, " es igual a: ",  numero_cuadrado % d)
if numero_cuadrado % d == 1:
    print(" es un número compuesto ")
else:
    print(" es un número primo ")


