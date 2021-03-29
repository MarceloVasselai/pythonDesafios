salario = float(input('Qual é o valor do salário (R$): '))
aumento = float(input('Qual é o aumento do salário (%): '))

print('O valor do salário é de R$ {:.2f} e com o aumento de {:.2f}% o salário ficará em R$: {:.2f}.'.format(salario,aumento,salario+(salario*aumento)/100))
