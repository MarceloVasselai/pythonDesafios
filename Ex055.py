menorpeso=1000
maiorpeso=0

for c in range(0,5):
    peso = int(input('Informe o peso da {}ª pessoa: '.format(c+1)))

    if peso < menorpeso:  menorpeso = peso
    if peso > maiorpeso:  maiorpeso = peso

print('O menor peso foi: {} enquanto o maior peso foi: {}'.format(menorpeso,maiorpeso))