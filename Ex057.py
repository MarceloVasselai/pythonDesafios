genero = str(input('Digite o Sexo (M/F): ')).strip().upper()[0]

while genero not in ['M','F']:
    genero = str(input("Dados inválidos, favor informar o Gênero: ")).strip().upper()[0]
print('Gênero {} registrado com sucesso'.format(genero))
