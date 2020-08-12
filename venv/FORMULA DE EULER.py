limite = int(input(" ingresar limite para aproximación de número E: "))
sumatoria = 0
formula = 1
i = 0
while i <= limite:
    factorial = 1
    for j in range(2, i +1):
        factorial *= j
    formula = 1 / factorial
    sumatoria += formula
    i += 1
print(" respuesta valor de E: ", sumatoria)