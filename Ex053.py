frase = str(input('Informe um Texto: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print('palíndromo')
else:
    print('não é palíndromo')
