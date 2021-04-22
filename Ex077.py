palavras=('televisao','jornal','cadeira','mouse','monitor','mesa','ovo')

for n in palavras:
    print(f'\n Na palavra {n.upper()} temos as seguintes vogais: ', end='')
    for l in n:
        if l.lower() in 'aeiou':
            print(l, end='')