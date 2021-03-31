ano = int(input('Digite o ano: '))
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('É um ano bissexto')
else:
    print('Não é bissexto')