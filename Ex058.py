import random
tent = 0

while tent >= 0:
    num = random.randint(0,3)
    numero = int(input('Digite o Número: '))
    tent += 1

    if num == numero:
        print('Acertou o número {} após {} tentativas'.format(numero,tent))
        tent = -1

