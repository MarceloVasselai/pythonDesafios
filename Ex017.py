import math

#tradicional
cat_o = float(input('Informe o Cateto Oposto = '))
cat_a = float(input('Informe o Cateto Adjacente = '))
hipot = (cat_o ** 2 + cat_a ** 2)  ** (1/2)
print('O valor do Cateto Oposto é {:.2f}, do Cateto Adjacente é {:.2f}, logo a Hipotenusa será {:.2f}'.format(cat_o,cat_a,hipot))

print('')
print('Agora usando o Import Math')
print('2')

#import math
cat_o = float(input('Informe o Cateto Oposto = '))
cat_a = float(input('Informe o Cateto Adjacente = '))
hipot = math.hypot(cat_o,cat_a)
print('O valor do Cateto Oposto é {:.2f}, do Cateto Adjacente é {:.2f}, logo a Hipotenusa será {:.2f}'.format(cat_o,cat_a,hipot))

