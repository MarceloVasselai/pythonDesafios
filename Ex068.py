from random import randint
vitorias=0
while True:

    p1 = int(input('Digite um número: '))
    comp = randint(0,10)
    soma = p1 + comp
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print (f'Você escolheu {p1} e o Computador {comp}. O Resultado foi {soma} ',end='')
    print ('e deu PAR' if soma % 2 == 0 else 'e deu Ímpar')

    if pi == 'P':
        if soma % 2 == 0:
            print('Você Venceu')
            vitorias += 1
        else:
            print('Você Perdeu')
            break
    elif pi == 'I':
        if soma % 2 == 1:
            print('Você Venceu')
            vitorias += 1
        else:
            print('Você Perdeu')
            break
    print('Vamos tentar novamente ?')
print(f'Fim do Par ou Ímpar! Ganhou por {vitorias} vez(es)')