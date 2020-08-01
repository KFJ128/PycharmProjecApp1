nota_1 = int(input(" leer primera nota del estudiante: "))
nota_2 = int(input(" leer segunda nota del estudiante: "))
nota_3 = int(input(" leer tercera nota del estudiante: "))
nota_4 = int(input(" leer cuarta nota del estudiante: "))
nota_5 = int(input(" leer quinta nota del estudiante: "))
promedio = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) / 5
if promedio >= 7:
     print(" su promedio es de: ",  promedio, " por ende el estudiante pasa de año ")
else:
     print(" su promedio es de:",  promedio,  "por ende el estudiante no pasa de año ")
