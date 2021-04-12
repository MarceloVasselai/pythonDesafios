n = cont = soma = 0
while n != 999:
    n = int(input('Informe um número [999 p/ sair]: '))
    if n != 999:
        soma += n
        cont += 1
print('A soma foi {}'.format(soma))
print('Total de {} números'.format(cont))