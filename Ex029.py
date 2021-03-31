velocidade = int(input('Qual a velocidade do carro: '))
excedeu = velocidade - 80

if velocidade <= 80:
    print('Não há multa')
else:
    print('Velocidade de {} Km/h, ultrapassou em {} Km e a multa será de R$ {:.2f}'.format(velocidade,excedeu,excedeu * 7))
    print('Blz?')