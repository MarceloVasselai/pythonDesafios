continuar = 'S'
p18 = 0
homens = 0
mulheres = 0

while continuar == 'S':

    idade = int(input('Informe a idade: '))
    sexo = str(input('Qual o gênero [M/F] ?:  ')).upper()

    if idade > 18:
        p18 += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres += 1
    else:
        print('Parâmetros inválidos')

    continuar = str(input('Deseja continuar [S/N] ?:  ')).upper()

    if continuar == 'N':
        print('Foram {} pessoas com mais de 18 anos, foram {} homens cadastrados e {} mulher com menos de 20 anos'.format(p18,homens,mulheres))