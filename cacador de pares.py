
qtd = int(input("Quantos números deseja digitar? "))

numeros = []

for i in range(qtd):
    num = int(input("Digite um número: "))
    numeros.append(num)

pares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)

print("Todos os números:", numeros)
print("Números pares:", pares)
print("Quantidade de pares:", len(pares))
