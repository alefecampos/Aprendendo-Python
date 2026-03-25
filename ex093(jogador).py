#aproveitamento de jogador de futebol
#ler nome do jogador, quantas partidas ele jogou, e quantos gols fez em cada partida. Guardar isso num dicionário
#incluindo o total de gols feitos no campeonato
print('-='*10)
print('BEM VINDO À CBF')
print('-='*10)
print('Insira os dados para acompanhar o campeonato')
#criando os dicionários
cadastro = {}
cadastro['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
#gols entra como lista, para ter como somar depois.
gols = list()
cadastro['gols'] = gols
#nao precisava criar uma variavel para o total. Poderia ser um dicionário
#jogador['total'] = sum(partidas)
totgols = 0
#laço para registrar gols por partida
for c in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {c+1}? '))
    gols.append(gol)
    totgols += gol
#resultado
cadastro['totgols'] = totgols
#for k, v in jogador.items()
#   print(f'o campo {k} tem o valor {v}')
print(f'{cadastro["nome"]}, {len(cadastro["gols"])}, {cadastro["gols"]}, {cadastro["totgols"]}')
print(gols)
print(cadastro)
