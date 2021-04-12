continua = 'S'
maior = cont = menor = media = soma = 0

while continua in 'Ss':
    num = int(input('Informe um número: '))
    soma += num
    cont += 1

    if cont == 1: maior = menor = num
    else:
        if num > maior: maior = num
        if num < menor: menor = num

    continua = str(input('Deseja continuar [S/N]: ')).upper()

print('O maior número é {}, o menor número é {} e a média é {:.2f}'.format(maior,menor, soma/cont))
