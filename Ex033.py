n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

lista = [n1,n2,n3]

print('Mínimo: {}'.format(min(lista)))
print('Máximo: {}'.format(max(lista)))

print('** OU **')

if n1 <= n2 and n1 <= n3:
    print('O menor número é: {}'.format(n1))
elif n2 <= n1 and n2 <= n3:
    print('O menor número é: {}'.format(n2))
elif n3 <= n1 and n3 <= n2:
    print('O menor número é: {}'.format(n3))

if n1 >= n2 and n1 >= n3:
    print('O maior número é: {}'.format(n1))
elif n2 >= n1 and n2 >= n3:
    print('O maior número é: {}'.format(n2))
elif n3 >= n1 and n3 >= n2:
    print('O maior número é: {}'.format(n3))