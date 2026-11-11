compras = []
item = input("Item(fim pra parar): ")
while item != "fim":
        compras.append(item)
        item = input("Item(fim pra parar): ")
print("Sua lista:" , compras)
print("Total de itens:", len(compras))