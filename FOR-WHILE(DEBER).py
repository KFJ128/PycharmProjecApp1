n = int(input(" leé valor: "))
p1 = 0
p2 = 0
p3 = 0
aproximacion = 1
for i in range(1, n+1, 1):
    p1 = (2 * i) / (2 * i -1)
    p2 = (2 * i) / (2 * i +1)
    p3 = p1 * p2
    aproximacion *= p3
    print(" aproximación a pi en el método Producto de Wallis: ", aproximacion)