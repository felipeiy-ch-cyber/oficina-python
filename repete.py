
palavras = []
repetidas = 0

for i in range(6):
    palavra = input("Digite uma palavra: ")

    if palavra not in palavras:
        palavras.append(palavra)
    else:
        repetidas += 1

print("Lista final:", palavras)
print("Repetidas descartadas:", repetidas)
