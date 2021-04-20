v9 = v3 = vp = 0
n1 = input('Digite o valor 1: ')
n2 = input('Digite o valor 2: ')
n3 = input('Digite o valor 3: ')
n4 = input('Digite o valor 4: ')

print (f'Os valores são: {n1}, {n2}, {n3}, {n4}')
tupla = (n1,n2,n3,n4)

for cont in range(0,len(tupla)):
    if tupla[cont] == '9':
        v9 += 1

for cont in range(0,len(tupla)):
    if tupla[cont] == '3':
        v3 = cont + 1

for cont in range(0,len(tupla)):
    if int(tupla[cont]) % 2 == 0:
        vp += 1

print(f'O número 9 apareceu {v9} vezes')
print(f'O número 3 apareceu na {v3}ª posição')
print(f'Os números pares digitados foram {vp}')