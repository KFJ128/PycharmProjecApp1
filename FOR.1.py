for i in range(20, 0, -1):
    print(" informes del año: ", i)
#factorial de un numero
factorial = int(input(" poner el valor a factorial: "))
for i in range(1, factorial, 1):
    factorial *= i
    print(" factorial es igual: ", factorial)

#cuadrado de un número
n = int(input(" leer valor: "))
respuesta = 0
for i in range(1, 2 * n, 2):
    respuesta += i
    print(" cuadrado del número es:", respuesta)