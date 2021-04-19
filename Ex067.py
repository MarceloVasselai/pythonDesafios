tabuada = 0
n = 0
while tabuada >= 0:
    tabuada=int(input('Informe a Tabuada: '))
    n = 0
    while n >= 0 and n <=10 and tabuada > 0:
        print('{} * {} = {}'.format(tabuada,n,tabuada*n))
        n += 1
print('FIM')