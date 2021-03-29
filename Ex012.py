preco = float(input('Qual o preço do Produto: '))
desconto = float(input('Qual é o desconto do Produto: '))

print('O valor do produto é de R$ {:.2f} e com o desconto de {:.2f}% ficará em R$: {:.2f}.'.format(preco,desconto,preco-(preco*desconto)/100))
