camisetas = int(input(" valor final de compra de camisetas: "))
zapatos = int(input(" valor final de compra de zapatos: "))
pantalones = int(input(" valor final de compra de pantalones: "))
chompas = int(input(" valor final de compra de chompas: "))
medias = int(input(" valor final de compra de medias: "))
#sumar el valor total de la compra
total = camisetas + zapatos + pantalones + chompas + medias
if total <= 75:
    print(" valor a pagar sin descuentos es. ", total)
else:
    total = total - (total *0.2)
    print(" valor a pagar con descuentos es. ", total)
