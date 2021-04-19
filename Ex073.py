times = ('Flamengo','Internacional','Atlético-MG','São Paulo','Fluminense','Grêmio','Palmeiras','Santos','Athletico-PR','Bragantino','Ceará','Corinthians','Atlético Goianiense','Bahia','Sport','Fortaleza EC','Vasco da Gama','Goiás','Coritiba','Botafogo')
print('{:-^100}'.format('TIMES DO BRASILEIRÃO'))
print(times)
print('')
print('{:-^100}'.format('OS 5 MELHORES TIMES'))
print(times[0:5])
print('')
print('{:-^100}'.format('OS 4 PIORES'))
print(times[-4:])
print('')
print('{:-^100}'.format('OS TIMES EM ORDEM ALFABÉTICA'))
print(sorted(times))
print('')
print('{:-^100}'.format('EM QUE POSIÇÃO ESTÁ O TRICOLOR DO MORUMBI'))

for cont in range(0,len(times)):
    if times[cont] == 'São Paulo':
        print (f'O {times[cont]} está na posição {cont+1}')