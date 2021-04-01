portugues =float(input('Nota de Portugues: '))
matematica=float(input('Nota de Matematica: '))
media=(portugues + matematica) / 2

if media < 5:
   print('Sua media foi {}, ou seja, menor do que 5.0, portanto vc foi REPROVADO'.format(media))
elif media >= 5 and media < 7:
    print('Sua media foi {}, ou seja, entre 5.0 e 6.9, portanto vc foi RECUPERAÇÃO'.format(media))
elif media >= 7:
    print('Sua media foi {}, ou seja, maior do que 7.0, portanto vc foi APROVADO'.format(media))

