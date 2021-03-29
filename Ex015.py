km_percorrido = float(input('Km percorrido: '))
valor_km = float(input('Valor por KM: '))
qt_dias = float(input('Qtde de Diárias: '))
valor_diaria = float(input('Valor por dia: '))

print('O preço a pagar será de R$ {:.2f} pelos {:.1f} Km percorridos + R$ {:.2f} por qtde diárias {:.2f}, totalizando R$ {:.2f}'
    .format(km_percorrido*valor_km,km_percorrido,qt_dias*valor_diaria,qt_dias,km_percorrido*valor_km + qt_dias*valor_diaria))
