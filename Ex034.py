salario=float(input('Informe o salário: '))

if salario > 1250:
    print('O seu salário é {:.2f} e o aumento será de {:.2f}, totalizando {:.2f}'.format(salario,salario*0.10,salario+(salario*0.10)))
else:
    print('O seu salário é {:.2f} e o aumento será de {:.2f}, totalizando {:.2f}'.format(salario,salario*0.15,salario+(salario*0.15)))
