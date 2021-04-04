preco_normal=float(input('Informe o valor do produto: '))
tipo=input('Informe o Tipo de Pagamento: ')

avd=preco_normal-(preco_normal * 0.10)
avc=preco_normal-(preco_normal * 0.05)
dxc=preco_normal
txm=preco_normal+(preco_normal * 0.20)

if tipo == 'avd':
    print('Valor do Produto {:.2f}, desconto de {:.2f} e o valor total {:.2f}'.format(preco_normal,preco_normal * 0.10,avd))
elif tipo == 'avc':
    print('Valor do Produto {:.2f}, desconto de {:.2f} e o valor total {:.2f}'.format(preco_normal,preco_normal * 0.05,avc))
elif tipo == 'dxc':
    print('Valor do Produto {:.2f} e sem desconto'.format(dxc))
elif tipo == 'txm':
    print('Valor do Produto {:.2f}, acréscimo de {:.2f} e o valor total {:.2f}'.format(preco_normal,preco_normal * 0.20,txm))
else:
    print('Tipo não Existe')
