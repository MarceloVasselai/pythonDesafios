from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for c in range(1,9):

    nasc = int(input( 'Em que a ano a {}ª pessoa nasceu: '.format(c)))
    idade = atual - nasc

    if idade >= 21:
        print('A {}ª pessoa é Maior de Idade'.format(c))
        totmaior += 1
    else:
        print('A {}ª pessoa é Menor de Idade'.format(c))
        totmenor += 1

print('Total de {} pessoas maior de idade'.format(totmaior))
print('Total de {} pessoas menor de idade'.format(totmenor))

