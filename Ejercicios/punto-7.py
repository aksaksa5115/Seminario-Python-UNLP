# Escribe un programa que solicite al usuario una lista de palabras. Luego, construí una
# oración uniendo únicamente las palabras que tengan más de 3 letras, separadas por
# espacios. Las palabras cortas deben ser excluidas del resultado final.
palabras = []
word = input("ingrese palabra: ")
while word != "end":
    palabras.append(word)
    word = input("ingrese palabra: ")

frase = ""
for i in palabras:
    if len(i) > 3:
        frase = frase + i + " "
        
print(frase)