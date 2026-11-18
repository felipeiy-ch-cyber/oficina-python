
pontuacoes = []

for i in range(5):
    nota = int(input("Digite uma pontuação: "))
    pontuacoes.append(nota)

media = sum(pontuacoes) / 5

acima = []

for nota in pontuacoes:
    if nota > media:
        acima.append(nota)

print("Pontuações:", pontuacoes)
print("Média:", media)
print("Acima da média:", acima)
print("Quantidade acima da média:", len(acima))

