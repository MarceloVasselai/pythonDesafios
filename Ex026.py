frase = input('Digite uma frase: ')

print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na casa {} '.format(frase.find('A')))
print('A letra A aparece pela última vez na casa {} '.format(frase.rfind('A')))
