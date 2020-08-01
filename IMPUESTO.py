sueldo = int(input(" poner el sueldo de ganancia: "))
interes = int(input(" poner el interes: "))
aportaciones_al_iess = int(input(" poner aportaciones al iess: "))
gastos_de_hogar = int(input(" gastos dentro del año en el hogar: "))
ip = int(input(" ip: "))
sueldo = sueldo * 12
interes = (sueldo * 0.095) - sueldo
interes = sueldo
sueldo = sueldo - aportaciones_al_iess
total_de_gatos_en_todo_el_año = (sueldo + ip + gastos_de_hogar) * 12
if total_de_gatos_en_todo_el_año <= 1131500:
 print (" total de gastos anuales:", total_de_gatos_en_todo_el_año, " con un impuesto = $0  ")

elif total_de_gatos_en_todo_el_año > 1131500 and total_de_gatos_en_todo_el_año <= 1441600:
 total_de_gatos_en_todo_el_año = total_de_gatos_en_todo_el_año
 print(" total de gastos anuales:", total_de_gatos_en_todo_el_año, " con un impuesto = $0  ")

elif total_de_gatos_en_todo_el_año > 1441600 and total_de_gatos_en_todo_el_año <= 1801800:

 total_de_gatos_en_todo_el_año = total_de_gatos_en_todo_el_año + 155
 print(" total de gastos anuales: ", total_de_gatos_en_todo_el_año, " con impuesto = $155 ")

elif total_de_gatos_en_todo_el_año > 1801800 and total_de_gatos_en_todo_el_año <= 2163900:
 total_de_gatos_en_todo_el_año = total_de_gatos_en_todo_el_año + 515
 print(" total de gastos anuales:", total_de_gatos_en_todo_el_año, " con impuesto = $515 " )

elif total_de_gatos_en_todo_el_año > 2163900 and total_de_gatos_en_todo_el_año <= 4326800:
 total_de_gatos_en_todo_el_año = total_de_gatos_en_todo_el_año + 950
 print(" total de gastos anuales:", total_de_gatos_en_todo_el_año, " con impuesto = $950 ")

elif total_de_gatos_en_todo_el_año > 4326800 and total_de_gatos_en_todo_el_año <= 6488700:
 total_de_gatos_en_todo_el_año = total_de_gatos_en_todo_el_año + 4194
 print(" total de gastos anuales:", total_de_gatos_en_todo_el_año, " con impuesto =  $4194 ")

elif total_de_gatos_en_todo_el_año > 6488700 and total_de_gatos_en_todo_el_año > 8651600:
 total_de_gatos_en_todo_el_año = total_de_gatos_en_todo_el_año + 8518
 print(" total de gastos anuales:", total_de_gatos_en_todo_el_año, " con  impuesto =  $8518 ")

elif total_de_gatos_en_todo_el_año < 8651600 and total_de_gatos_en_todo_el_año > 11533800:
 total_de_gatos_en_todo_el_año = total_de_gatos_en_todo_el_año + 13925
 print(" total de gastos anuales:", total_de_gatos_en_todo_el_año,  " con impuesto =  $13925 ")

else:
 total_de_gatos_en_todo_el_año = total_de_gatos_en_todo_el_año + 22572
 print(" total de gastos anuales:", total_de_gatos_en_todo_el_año, " con  impuesto = $22572 ")

