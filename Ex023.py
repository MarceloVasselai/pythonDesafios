numero = input('Digite um número de 0 a 9999: ')
numero = str(numero).zfill(4)

unidade  = numero[3:4]
dezena  = numero[2:3]
centena = numero[1:2]
milhare = numero[0:1]

print('Unidade do número é: {}'.format(unidade))
print('Dezena do número é: {}'.format(dezena))
print('Centena do número é: {}'.format(centena))
print('Milhar do número é: {}'.format(milhare))