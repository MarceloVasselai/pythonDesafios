n1=int(input('informe o primeiro número: '))
n2=int(input('informe o segundo  número: '))
n3=int(input('informe o terceiro número: '))
n4=int(input('informe o quarto   número: '))
n5=int(input('informe o quinto   número: '))
n6=int(input('informe o sexto    número: '))
tot=0

if (n1 % 2) == 0: tot += n1
if (n2 % 2) == 0: tot += n2
if (n3 % 2) == 0: tot += n3
if (n4 % 2) == 0: tot += n4
if (n5 % 2) == 0: tot += n5
if (n6 % 2) == 0: tot += n6

print('Soma: {}'.format(tot))