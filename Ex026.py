frase = input('Digite uma frase: ')
tot_a = frase.count('A')
prim_vez = frase.find('A')
ult_vez = frase.rfind('A')

print('A letra A aparece {} vezes'.format(tot_a))
print('A letra A aparece pela primeira vez na casa {} '.format(prim_vez))
print('A letra A aparece pela última vez na casa {} '.format(ult_vez))
