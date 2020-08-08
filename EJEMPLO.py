#conteo
numero = input(" leer el número: ")
resultado = len(numero)
i = 0
while i <= resultado-1:
    i += 1
print(" digitos igual: ", i)






# capicua
numero = int(input(" escribir el valor a invertir  "))
centena = numero // 100
residuo = numero % 100
decena = residuo // 10
unidad = residuo % 10
u = str(unidad)
d = str(decena)
c = str(centena)
t = int(u + d + c)
if numero == t:
    print(" si es capicua: ", unidad, decena, centena)
else:
    print(" no es un número capicua:", unidad, decena, centena)
