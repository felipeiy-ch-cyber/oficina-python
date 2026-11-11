pontos = []

for i in range(5):
    pontos.append(int(input("Pontos: ")))

media = sum(pontos) / len(pontos)

print("Média:", media)

cont = 0

for p in pontos:
    if p > media:
        print("Pontuação acima da média:", p)
        cont += 1

print("Quantidade acima da média:", cont)
