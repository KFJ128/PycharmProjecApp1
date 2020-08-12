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


#leer un vector de 5 elementos
vector = []
n = 5
for i  in range(0, n):
    vector.append(int(input(" ingrese el valor: ")))
#mostrar valor del vector
# 1.- manera
for valor in vector:
    print(" valor del vector:", valor)
#2._ manera 2
print(" el vector tiene ", len(vector), " elemento ")
for i in range(0, len(vector)):
    print(" elemento del vector ", i, " = ", vector[i])
    #manera inversa
print(" el vector tiene ", len(vector), " elemento ")


for i in range(0, len(vector)-1, -1, -1):
    print(" elemento del vector ", i, " = ", vector[i])