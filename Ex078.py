lista = list()
maior = menor = 0
for pos in range(0,5):
    n = input(f'Digite um valor para a posição {pos}: ')
    lista.append(pos)

print (f'Você digitou os valores {lista}')
print (f'O maior valor foi: {max(lista)}')
print (f'O menor valor foi: {min(lista)}')
