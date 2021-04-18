while True:
    tabuada=int(input('Informe a Tabuada: '))
    print ('-+' * 30)
    if tabuada < 0:
        break
    for n in range (1,11):
        print(f'{tabuada} * {n} = {tabuada * n}')
        n += 1
    print('+-' * 30)
print('FIM')