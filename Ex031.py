distancia = float(input('Qual a distância da viagem: '))

if distancia <= 200:
    print('O valor passagem até 200 Km será: R$ {}'.format(distancia*0.50))
else:
    print('O valor passagem com mais de 200 Km será: R$ {}'.format(distancia*0.45))
    print('Blz?')