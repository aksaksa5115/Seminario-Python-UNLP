# Escribe un programa que simule una caja registradora:
# el usuario ingresa precios de productos de a uno.
# Cuando ingresa 0, el programa se detiene y muestra el total acumulado.
# Nota: utilizá la sentencia break cuando haga falta.


total = 0
precio = int(input("ingrese precio: " ))
while precio != 0:
    total += precio
    precio = int(input("ingrese precio: " ))
print(total)
