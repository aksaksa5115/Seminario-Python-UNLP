# Modifica el ejercicio 4 para que, en lugar de imprimir los números, genere dos listas:
# una con los múltiplos de 5 y otra con el resto de los números. Imprimí ambas listas al
# finalizar.

number = int(input("ingrese numero : "))
multiplos = []
numeros = []
for i in range(1, number + 1):
    if i % 5 == 0:
        multiplos.append(i)
    else: numeros.append(i)
print(multiplos)
print(numeros)