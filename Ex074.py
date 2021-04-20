from random import randint

n1 = randint(0,100)
n2 = randint(0, 100)
n3 = randint(0, 100)
n4 = randint(0, 100)
n5 = randint(0, 100)

print (f'Os valores são: {n1}, {n2}, {n3}, {n4}, {n5}')

tupla = (n1,n2,n3,n4,n5)

print (f'O número máximo foi {max(tupla)}')
print (f'O número mínimo foi {min(tupla)}')