lista = []
lista2 = []
lista3 = []
totpessoas = maiorpeso = menorpeso = 0
while True:
    lista.append(str(input('Informe o nome: ')))
    lista.append(int(input('Informe o peso: ')))
    totpessoas += 1
    cont = input('Quer continuar [S/N]: ').upper()
    for pos in range(0, len(lista)):
        if pos % 2 == 0:
            lista2.append(lista[pos])

        else:
            lista3.append(lista[pos])
    if cont == 'N':
        break

maiorpeso = max(lista3)
menorpeso = min(lista3)

print (f'Você cadastrou: {totpessoas} pessoas')
print (f'O maior peso foi : {maiorpeso}')
print (f'O menor peso foi : {menorpeso}')