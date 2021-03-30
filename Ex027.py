nome = str(input('Digite um Nome: ')).strip()
primeiro_nome = nome.split()
ultimo_nome = nome.rsplit()
pos_ult_nome = int(nome.count(' '))

print('O nome digitado foi: {}'.format(nome))
print('O primeiro nome foi: {} '.format(primeiro_nome[0]))
print('O último nome foi: {} '.format(ultimo_nome[pos_ult_nome]))

print('Outra opção')
print('O último nome foi: {} '.format(primeiro_nome[len(primeiro_nome)-1]))
