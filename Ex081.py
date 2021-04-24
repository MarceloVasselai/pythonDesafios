numeros = []
while True:
    numeros.append(int(input('Informe um número: ')))
    cont = str(input('Deseja continuar ? [S/N] ')).upper()
    if cont == 'N':
        break
print(f'Você informou {len(numeros)} valores')
numeros.sort(reverse=True)
print(f'Os números em ordem descrescente são {numeros}')
if 5 in numeros:
    print('o número 5 está na lista')
else:
    print('o número 5 não está na lista')