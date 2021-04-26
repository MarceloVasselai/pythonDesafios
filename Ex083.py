expr = str(input('Digite a Expressão: '))
pilha = []
for caract in expr:
    if caract == '(':
        pilha.append('(')
    elif caract == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')

