listag = []
listap = []
listai = []

for pos in range(1, 8):
    n = int(input(f'Digite o {pos}º valor: '))
    listag.append(n)
    if n % 2 == 0:
        listap.append(n)
    else:
        listai.append(n)

print(f'Todos os números digitados foram {listag}')
print(f'Os números pares digitados foram {listap}')
print(f'Os números ímpares digitados foram {listai}')