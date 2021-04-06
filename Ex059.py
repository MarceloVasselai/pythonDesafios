n=0
maior=0
while n==0:
    n1=int(input('Digite o primeiro número: '))
    n2=int(input('Digite o segundo número: '))

    op = input('Digite [1]somar [2]multiplicar [3]maior [4]novos números [5]sair do programa. Qual a sua opção: ')

    if op == '1':
        print('A Soma entre {} e {} resulta em {}'.format(n1,n2,n1+n2))
    elif op == '2':
        print('A Multiplicação entre {} e {} resulta em {}'.format(n1,n2,n1*n2))
    elif op == '3':
        if n1>n2: maior=n1
        else: maior=n2
        print('O maior entre {} e {} é o número: {}'.format(n1,n2,maior))
    elif op == '4':
        print('Informe os novos números')
    elif op == '5':
        n=1



