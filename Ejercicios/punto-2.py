# Escribe un programa que solicite al usuario una cantidad de segundos y
# muestre cuántas horas, minutos y segundos equivalen.
# Por ejemplo, 3661 segundos son 1 hora, 1 minuto y 1 segundo.

cant_seconds = int(input("ingrese una cantidad de segundos: "))
horas = cant_seconds // 3600
cant_seconds = cant_seconds - horas * 3600
minutos = cant_seconds // 60
cant_seconds = cant_seconds - minutos * 60

print("cantidad de horas:",horas,
"cantidad de minutos:",minutos,
"cantidad de segundos:",cant_seconds)
