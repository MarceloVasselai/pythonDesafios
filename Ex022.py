nome = input('Digite o seu nome: ')
nome_s_espaço = nome.replace(' ','')
tot_sem_espacos = int(len(nome_s_espaço))
primeiro_nome = nome.split()

tot_espacos = nome.count(' ')
sem_espaco_II = int(len(nome)) - int(tot_espacos)

print('Nome em maiúsculo: ' + nome.upper())
print('Nome em minúsculo: ' + nome.lower())
print('Total de Letras no nome sem Espaços I : ' + str(tot_sem_espacos))
print('Total de Letras no nome sem Espaços II: ' + str(sem_espaco_II))
print('Total de Letras no primeiro nome: {}'.format(len(primeiro_nome[0])))




