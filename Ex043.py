peso=float(input('Informe o seu peso: '))
altura=float(input('Informe a sua altura: '))

imc = peso/(altura*altura)

if imc <= 18.5:
    print('IMC de {:.2f} ...está Abaixo do Peso'.format(imc))
elif imc > 18.5 and imc <= 25 :
    print('IMC de {:.2f} ...está com o Peso Ideal'.format(imc))
elif imc > 25 and imc <= 30 :
    print('IMC de {:.2f} ...está com Sobrepeso'.format(imc))
elif imc > 30 and imc <= 40:
    print('IMC de {:.2f} ...está com Obesidade'.format(imc))
elif imc > 40:
    print('IMC de {:.2f} ...está co Obesidade Mórbida'.format(imc))
