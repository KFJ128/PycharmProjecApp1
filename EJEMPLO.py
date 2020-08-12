#conteo
numero = input(" leer el número: ")
resultado = len(numero)
i = 0
while i <= resultado-1:
    i += 1
print(" digitos igual: ", i)






# capicua
numero = int(input(" escribir el valor a invertir  "))
for i in (numero, numero):
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




#tabla de multiplicar:
numero = int(input(" introducir el número: "))
for j in range(1, 11):
    for i in range(1, 11):
        print(numero, " x ", i, " = ", (numero * i))
    numero += 1



#multiplicacion
valor_a = int(input(" add número para a: "))
valor_b = int(input(" add número para b: "))
i = 1
suma = 0
while i <= valor_b:
    suma += valor_a
    i += 1
print(suma)