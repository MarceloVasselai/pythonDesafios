from random import randint
from time import sleep
lista = list()
jogos = list()
print('$_' * 10,'MEGA SENA','$_' * 10)
qtde = int(input('Quantos jogos você quer que eu sorteie: '))
tot = 1
while tot <= qtde:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('$_' * 10,f'SORTEANDO {qtde} Jogos','$_'* 10)
for i,l in enumerate(jogos):
    print(f'Jogo {i+1}:{l}')
    sleep(1)
print('$_' * 10,'BOA SORTE','$_' * 10)