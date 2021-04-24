num = list()
while True:
    n=int(input('Digite um Valor: '))
    if n not in num:
        num.append(n)
        print('adicionado')
    else:
        print('já consta na lista')
    r = str(input('quer continuar? [S/N] '))
    if r in 'Nn':
        break
num.sort()
print(f'Os números digitados foram: {num} ')