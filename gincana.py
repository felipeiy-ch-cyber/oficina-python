
nomes = ["Ana", "Leo", "Bia", "Rui"]
pontos = [30, 55, 42, 18]

maior = pontos[0]
indice = 0

for i in range(len(pontos)):
    if pontos[i] > maior:
        maior = pontos[i]
        indice = i

print("Quem fez mais pontos:", nomes[indice])
print("Pontuação:", maior)
