tot=0
for c in range(0,6):
    n = int(input('Informe o {}º número: '.format(int(c)+1)))
    if (n % 2) == 0: tot += n
print('Soma: {}'.format(tot))
