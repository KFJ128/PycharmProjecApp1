nc1 = int(input(" leer el primer digito de la cedula: "))
nc2 = int(input(" leer el segundo digito de la cedula: "))
nc3 = int(input(" leer el tercero digito de la cedula: "))
nc4 = int(input(" leer el cuarto digito de la cedula: "))
nc5 = int(input(" leer el quinto  digito de la cedula: "))
nc6 = int(input(" leer el sexto  digito de la cedula: "))
nc7 = int(input(" leer el septimo  digito de la cedula: "))
nc8 = int(input(" leer el octavo  digito de la cedula: "))
nc9 = int(input(" leer el noveno  digito de la cedula: "))
a = nc1 * 2
if a > 9:
   a = a - 9


b = nc3 * 2
if b > 9:
   b = b - 9


c = nc5 * 2
if c > 9:
   c = c - 9


d = nc7 * 2
if d > 9:
   d = d - 9


e = nc9 * 2
if e > 9:
   e = e - 9
#suma de numeros impares:
impares = (a + b + c + d + e)

#suma de pares
pares = (nc2 + nc4 + nc6 + nc8)

#suma de pares e impares
total = (pares + impares)
print(" total: ", total)

total %= 10
total = 10 - total
print(f"Dígito verificador es: ", total)




