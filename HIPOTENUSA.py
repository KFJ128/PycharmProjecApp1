cateto_opuesto = int(input(" leer el cateto opuesto: "))
cateto_adyacente = int(input(" leer el cateto adyacente: "))
 #calcular la hiptenusa mediante el teorema de piagoras
import math
hipotenusa = math.sqrt(cateto_adyacente ** 2 + cateto_opuesto ** 2)
print(" la hipotenusa aplicando el teorema de pitagoras es: ",  hipotenusa)
