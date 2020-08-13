


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





vector1 = []
n = int(input(" leer el limite: "))
for i in range(0, n):
    vector1.append(int(input(" escribir valores del vector: ")))
print(" el vector tiene: ", len(vector1), " elementos ")
for j in range(0, len(vector1)):
    print(" elemento del vector ", j,":",  vector1[j])


