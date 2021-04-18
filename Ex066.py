cont = soma = 0
while True:
    n = int(input('Informe um número [999 p/ sair]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} totalizam {soma}')
