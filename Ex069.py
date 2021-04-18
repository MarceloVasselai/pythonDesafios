p18 = homens = mulheres = 0
while True:
    idade = int(input('Informe a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o gênero [M/F] ?:  ')).strip().upper()[0]
    if idade >= 18:
        p18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N] ?:  ')).strip().upper()[0]
    if continuar == 'N':
        break
print('Foram {} pessoas com mais de 18 anos, foram {} homens cadastrados e {} mulher com menos de 20 anos'.format(p18,homens,mulheres))