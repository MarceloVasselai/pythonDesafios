import math

angulo=float(input('Informe um ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O ângulo informado foi {}, seu seno é {:.2f}, o cosseno {:.2f} e a tangente {:.2f}'.format(angulo,seno,cosseno,tangente))