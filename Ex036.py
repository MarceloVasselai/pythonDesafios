valor=float(input('Valor da casa: '))
salario=float(input('Salário do comprador: '))
anos=float(input('Qtde anos: '))

valor_max = salario * 0.3
valor_prest = valor / (anos*12)

if int(valor_max) >= int(valor_prest):
    print('Empréstimo Autorizado !!!!')
else:
    print('Empréstimo Negado !!!!')
