palavra = input("Digite uma palavra: ")

for posicao in range(len(palavra)-1, -1, -1):
    print(posicao, palavra[posicao])