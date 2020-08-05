n = int(input(" leé valor: "))
p1 = 0
p2 = 0
p3 = 0
aproximacion = 1
for i in range(1, n+1):
    p1 = (2 * i) / (2 * i - 1)
    p2 = (2 * i) / (2 * i + 1)
    p3 = p1 * p2
    aproximacion *= p3
print(" aproximación a pi en el método Producto de Wallis: ", aproximacion)




#divir
dividendo = int(input(" leer el dividendo:"))
divisor= int(input(" leer el divisor:"))
cociente = 0
while dividendo >= divisor:
 dividendo -= divisor
 cociente = cociente + 1
#resultado
print("conciente: ", cociente)
print(" resto: ", dividendo)




 #numero primo
n = int(input("leer valor: "))
acum = 1
contt = 1
prom = 0
for i in range(1, n + 1, 1):
 cont = 0
 for j in range(1, n + 1, 1):
  if i % j == 0:
   cont += 1
  if cont == 2:
    acum += i
    contt += 1
prom = (acum / contt)
print(prom)







