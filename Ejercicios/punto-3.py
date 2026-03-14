# Crea un programa que solicite al usuario un número y muestre su tabla de
# multiplicar del 1 al 10 utilizando un bucle for.

number = int(input("ingrese el numero para ver su tabla: "))

for i in range(1, 11):
    print("indice:", i, "resultado:", number * i)
