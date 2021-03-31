print('-='*20)
print('Analisador de Triângulos')

r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r2:
    print('Os segmentos acima, formam um triângulo')
else:
    print('Os segmentos acima, não formam um triângulo')
