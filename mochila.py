mochila = ["Lapis","caderno","caderno"]
pergunta = input()
if pergunta in mochila: 
    print("Ja esta na mochila")
else:
    mochila.append(pergunta)
    print("Coloquei")