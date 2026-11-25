frase = input("Digite uma frase: n/")
vogais = "aeiou"
contador = 0
for letra in frase:
    if letra.lower()in vogais:
        contador += 1
        print("A frase digitada possui",contador,"vogais.")