n = int(input())
soma = 0

for i in range(n):
    nota = float(input())
    soma += nota

media = soma / n
print(f"{media:.2f}")