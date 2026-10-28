senha_certa = "1234"
tentativas = 0
aberto = False

while tentativas < 3:
    senha = input()
    tentativas += 1

    if senha == senha_certa:
        aberto = True
        break

if aberto:
    print("Aberto")
else:
    print("Bloqueado")