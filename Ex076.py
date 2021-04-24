lista = ('Caneta', 1.99,
         'Borracha', 1.99,
         'Apotador', 2,
         'Régua', 3,
         'Sulfite', 0.1,
         'Compasso', 2.32,
         'Transferidor', 111.99
         )
print (lista)
print ('-' * 50)
print (f'{"LISTAGEM DE PREÇOS":^40}')
print ('-' * 50)

for pos in range(0,len(lista)):
    if pos % 2 == 0:
        print (f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:>7.2f}')
print ('-' * 50)