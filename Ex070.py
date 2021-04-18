total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Qual o Produto: '))
    preco = float(input ('Informe o preço R$: '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM '))
print(f'Totalizando a compra em R$ {total:.2f}')
print(f'Temos {totmil} produto(s) acima de R$ 1.000')
print(f'O mais barato foi {barato} custando R$ {menor:.2f}')

