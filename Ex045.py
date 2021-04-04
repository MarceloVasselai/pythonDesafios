jog1=input('Jogador 1, digite o objeto...: ')
jog2=input('Jogador 2, digite o objeto...: ')

print('')
print('Jokenpô....')
print('')

if jog1 == jog2:
    print('Empate...')
elif (jog1 == 'Pedra' and jog2 == 'Tesoura') or\
        (jog1 == 'Papel' and jog2 == 'Pedra') or\
        (jog1 == 'Tesoura' and jog2 == 'Papel'):
    print('Vendedor Jogador 1')
elif (jog2 == 'Pedra' and jog1 == 'Tesoura') or\
        (jog2 == 'Papel' and jog1 == 'Pedra') or\
        (jog2 == 'Tesoura' and jog1 == 'Papel'):
    print('Vendedor Jogador 2')
else:
    print('Objeto digitado errado...')




