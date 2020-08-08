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


#E
n = int(input(" leer valor: "))
acum = 0
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
    fac = 1 / factorial
    acum += fac
print(acum)


 #numero primo
n = int(input("Leer valor: "))
acum = 1
contt = 1
prom = 0
for i in range(1, n+1):
    cont = 0
    for j in range(1, n+1):
        if i % j == 0:
            cont += 1
    if cont == 2:
       acum += i
       contt += 1
prom = (acum / contt)
print(" Pemerdio de números primos:", prom)



#new formula
e = int(input(" Leer valor: "))
resultado = 0
f1 = 1
f2 = 1
n1 = 0
n2 = 0
for m in range(0, e, 1):
    e = m
    n2 = (2 * e) + 1
    n1 = e
    for i in range(1, n1+1, 1):
        f1 *= i
    for j in range(1, n2+1, 1):
        f2 *= j
    resultado += ((2 ** e) * (f1 ** 2)) / f2
    f1 = 1
    f2 = 1
print(resultado)


#base exponente
base = int(input(" Leer base: "))
exponente = int(input(" Leer exponente: "))
resultado = base
t = 0
for i in range(1, exponente, 1):
    for j in range(1, base+1, 1):
        t += resultado
    resultado = t
    t = 0
print(" resultado: ", resultado)


#conteo de digitos.
numero =input(" leer el número: ")
numero2 = str(numero)
resultado = len(numero2)
print(resultado)



#tabla de multiplicar:
numero = int(input(" introducir el número: "))
for i in range(1, 11):
    print(numero, " x ", i, " = ", (numero * i))




#cedula
print("\nIntroduce 9 digitos de cédula")
sumaPar = 0
sumaImpar = 0
producto = 0
i = 1
while i < 10:
     digitos = int(input(f"Introduce dígito {i}: "))
     if i % 2 == 0:
          sumaPar += digitos
     else:
          producto = digitos * 2
          if producto > 9:
              producto -= 9
          sumaImpar += producto
     i += 1

sumaT = sumaPar + sumaImpar
mod = sumaT % 10
if mod != 0:
     mod = 10 - mod
     print(f"Dígito verificador es : ", mod)
else:
     print("Dígito verificador es: 0 ")

     # Factura con descuento del 10% si su monto es mayor a $100
     subtotal = 0
     i = 1
     while i != 0:
         total_productos = int(input("Ingrese total de productos: "))
         j = 1
         while j <= total_productos:
             producto = int(input("Valor producto : "))
             subtotal += producto
             j += 1
         fin_while = int(input(" digite 0 para terminar proceso:"))
         if fin_while == 0:
             i = 0

     if subtotal > 100:
         descuento = subtotal * 0.10
         subtotal -= descuento

     iva = subtotal * 0.12
     iva = round(iva, 2)
     total_pago = subtotal + iva
     total_pago = round(total_pago, 2)

     print(f"IVA: {iva} Total a pagar: {total_pago}")



# Factura con descuento del 10% si su monto es mayor a $100
subtotal = 0
i = 1
while i != 0:
     total_productos = int(input("Ingrese total de productos: "))
     j = 1
     while j <= total_productos:
         producto = float(input("Valor producto : "))
         subtotal += producto
         j += 1
     fin_while = int(input(" digite 0 para terminar proceso:"))
     if fin_while == 0:
          i = 0

if subtotal > 100:
    descuento = subtotal * 0.10
    subtotal -= descuento
iva = subtotal * 0.12
total_pago = subtotal + iva
print(" iva: ", iva)
print(" total a pagar: ", total_pago)



#conteo
numero =int(input(" leer el número: "))
numero2 = str(numero)
resultado = len(numero2)
resultado2 = int(resultado)
conteo = 0
for i in (0, resultado2-1, 1):
    conteo += i
print(conteo)

