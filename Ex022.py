nome = input('Digite o seu nome: ')
nome_s_espaço = nome.replace(' ','')
tot_sem_espacos = int(len(nome_s_espaço))
primeiro_nome = nome.split()

print('Nome em maiúsculo: ' + nome.upper())
print('Nome em minúsculo: ' + nome.lower())
print('Total de Letras sem Espaços: ' + str(tot_sem_espacos))
print('Primeiro Nome: {}'.format(len(primeiro_nome[0])))



