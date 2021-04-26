listat = list()
listai = list()
listap = list()

while True:
    num = int(input ('Digite um número: '))
    listat.append(num)
    if num % 2 == 0:
        listap.append(num)
    else:
        listai.append(num)

    cont = input('Quer continuar [S/N]: ').upper()

    if cont == 'N':
        break

print(f'a Lista completa é: {listat}')
print(f'a Lista de Pares é: {listap}')
print(f'a Lista de Ímpares é: {listai}')

