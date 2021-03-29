import random

aluno1 = str(input ('Informe o nome do aluno 1: '))
aluno2 = str(input ('Informe o nome do aluno 2: '))
aluno3 = str(input ('Informe o nome do aluno 3: '))
aluno4 = str(input ('Informe o nome do aluno 4: '))
alunos = [aluno1,aluno2,aluno3,aluno4]

sorteado = random.choice(alunos)
print ('O aluno sorteado foi: {}'.format(sorteado))



