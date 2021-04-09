cont=0
n = int(input('Digite o número: '))

while cont<(n-1):
    cont+=1
    if cont ==1:
        tot = n * cont
    else:
        tot = tot * cont

print ('O Fatorial do {} será: {}'.format(n,tot))

