numero=int(input('Informe o número: '))
tipo=input('Informe o tipo: ')

if tipo == 'binário':
    print('Você digitou {} e o valor binário é {}'.format(numero,bin(numero)))
elif tipo == 'octal':
    print('Você digitou {} e o valor octal é {}'.format(numero,oct(numero)))
elif tipo == 'hexadecimal':
    print('Você digitou {} e o valor hexadecimal é {}'.format(numero,hex(numero)))
else:
    print('Tipo Errado!')


