cedula = [1, 7, 2, 7, 6, 6, 6, 8, 3, 4]

cedula[0] = cedula[0] * 2
if cedula[0] > 9:
    cedula[0] -= 9

cedula[2] = cedula[2] * 2
if cedula[2] > 9:
    cedula[2] -= 9

cedula[4] = cedula[4] * 2
if cedula[4] > 9:
    cedula[4] -= 9

cedula[6] = cedula[6] * 2
if cedula[6] > 9:
    cedula[6] -= 9

cedula[8] = cedula[8] * 2
if cedula[8] > 9:
    cedula[8] -= 9

suma_pares = cedula[1]+cedula[3]+cedula[5]+cedula[7]

suma_impares = cedula[0] + cedula[2] + cedula[4] + cedula[6] + cedula[8]

suma_total = suma_pares + suma_impares

suma_total %= 10
if suma_total != 0:
    suma_total = 10 - suma_total
    print(f"Dígito verificador es: {suma_total}")
else:
    print(f"Dígito verificandor es : {suma_total}")

