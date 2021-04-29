matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somat = soma3 = somam = 0
for l in range(0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite uma valor para [{l},{c}]: '))
        if int(matriz[l][c]) % 2 == 0:
            somat = somat + matriz[l][c]
        if c == 2:
            soma3 = soma3 + matriz[l][c]
        print(l,somam)
        if l == 1:
            if somam < int(matriz[l][c]):
                somam = int(matriz[l][c])
print('+-'*30)
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print(f'A soma dos valores pares é: {somat}')
print(f'A soma dos valores da terceira coluna é: {soma3}')
print(f'O maior valor da segunda linha é: {somam}')