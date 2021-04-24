lista = []
for c in range(0,5):
    n = int(input('Informe um valor: '))
    if c == 0 or n > lista [-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor Adicionado na posição {pos} da Lista...')
                break
            pos += 1
print('-=' * 50)
print(f'Os valores digados foram {lista} ')