import random

resultado = 'VENCEU'

while resultado != 'PERDER':

    n1 = int(input('Digite um número: '))
    pi = str(input('Par ou Ímpar? [P/I]: ')).upper()
    n2 = random.randint(0,10)
    soma = n1 + n2
    if (soma % 2) == 0 and pi == 'I':
        print('Você Perdeu !!! Informou o número {} e o Computador {}, totalizando {}'.format(n1,n2,n1+n2))
        resultado = 'PERDER'
    elif (soma % 2) == 0 and pi == 'P':
        print('Você Ganhou !!! Informou o número {} e o Computador {}, totalizando {}'.format(n1,n2,n1+n2))
    elif (soma % 2) != 0 and pi == 'I':
        print('Você Ganhou !!! Informou o número {} e o Computador {}, totalizando {}'.format(n1,n2,n1+n2))
    elif (soma % 2) != 0 and pi == 'P':
        print('Você Perdeu !!! Informou o número {} e o Computador {}, totalizando {}'.format(n1,n2,n1+n2))
        resultado = 'PERDER'
