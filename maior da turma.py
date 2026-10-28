N = int(input())

maior = 0

for i in range(N):
    pontuacao = int(input())

    if pontuacao > maior:
        maior = pontuacao

print(maior)