numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito',
           'nove','dez','onze','doze','treze','catorze','quinze','dezesseTupis',
           'dezessete','dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um número [0-20]: '))
    if num >= 0  and num <= 20:
        print(f'Você informou o número {numeros[num]}')
        break
    else:
        print('Tente novamente....')