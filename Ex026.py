frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na casa {} '.format(frase.find('A')+1))
print('A letra A aparece pela última vez na casa {} '.format(frase.rfind('A')+1))
