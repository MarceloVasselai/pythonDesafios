import random

numero = int(input('Digite um Número: '))
sorteio = random.randint(0,3)

print('Sorteando um número...')

if numero == sorteio:
    print('BINGO')
else:
    print('Erroooouuu... tente outra vez!')
print('O computador pensou no número {} e você digitou {}!'.format(sorteio,numero))