numero = int(input(" escribir el valor a invertir  "))
centena = numero // 100
residuo = numero % 100
decena = residuo // 10
unidad = residuo % 10
print(" capicúa del numero : ",  unidad,  decena,  centena)
