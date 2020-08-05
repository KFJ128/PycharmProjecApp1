n = int(input(" Lee valor: "))
p1 = 0
p2 = 0
p3 = 0
aproximacion = 1
for i in range(1, n+1):
    p1 = (2 * i) / (2 * i - 1)
    p2 = (2 * i) / (2 * i + 1)
    p3 = p1 * p2
    aproximacion *= p3
print(" Aproximación a pi en el método producto de Wallis: ", aproximacion)




#divir
dividendo = int(input(" Leer el dividendo:"))
divisor= int(input(" Leer el divisor:"))
cociente = 0
while dividendo >= divisor:
 dividendo -= divisor
 cociente += 1
#resultado
print("Conciente: ", cociente)
print(" Resto: ", dividendo)




 #numero primo
n = int(input("Leer valor: "))
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
print(" Pemerdio de números primos:", prom)







