N = int(input())

tem_par = False

for i in range(1, N + 1):
    if i % 2 == 0:
        print(i)
        tem_par = True

if not tem_par:
    print("Nenhum")