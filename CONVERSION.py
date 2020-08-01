#conversion de tiempo
segundos = int(input(" escribir los segundos: "))
minutos = int(input(" escribir los minutos: "))
horas = int(input(" escribir los horas: "))
if segundos <= 59 and minutos <= 59:
    print(" conversion: ", " horas: ", horas, " minutos: ", minutos, " segundos ", segundos)
else:
    minutos = minutos + (segundos // 60)
    segundos = segundos % 60
    print(" segundos: ", segundos)
    if minutos <= 59:
        print(" minutos: ", minutos)
    else:
        horas = horas + (minutos // 60)
        minutos = minutos % 60
        print(" minutos: ", minutos)
        print(" horas: ", horas)
        print(" conversion: ", " horas: ", horas, " minutos: ", minutos, " segundos ",  segundos)
