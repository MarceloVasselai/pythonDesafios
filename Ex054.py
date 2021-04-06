for c in range(0,7):
    ano = int(input('Informe o ano de nascimento da {}ª pessoa: '.format(c+1)))
    if (2021-ano) < 21:
        print('A {}ª pessoa é Menor de Idade'.format(c+1))
    else:
        print('A {}ª pessoa é Maior de Idade'.format(c+1))



