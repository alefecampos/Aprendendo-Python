def jogador (nome='', gols=''):
    if nome == '':
        nome = 'desconhecido'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gols no campeonato.')

jogador(input('Digite o nome do jogador: '), input('Quantos gols ele fez? '))

