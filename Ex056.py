totidade=0
maisvelho=0
totmulheres=0

for c in range(0,4):
    nome  = input('Informe o nome da {}ª pessoa: '.format(c+1))
    idade = int(input('Informe a idade da {}ª pessoa: '.format(c+1)))
    sexo  = input('Informe sexo da {}ª pessoa: '.format(c+1))

    totidade+=idade
    if idade > maisvelho:  maisvelho = idade

    if sexo =='F' and idade <20: totmulheres+=1

print('a média de idade do grupo foi {}, sendo o mais velho {} e o total de mulheres com menos de 20 anos foi {}'.format(totidade/4,maisvelho,totmulheres))