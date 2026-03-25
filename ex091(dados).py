from random import randint
from time import sleep
print('-='*12)
print('QUE RUFEM OS TAMBORES...')
print('-='*12)
sleep(0.5)
print('Jogando os dados...')
sleep(0.5)
jogador = {}
for c in range(0, 4):
    jogador[f'{c}'] = randint(1, 6)
for k, v in jogador.items():
    print(f'O jogador {k} tirou: {v}')
    print('-' * 20)
    sleep(0.5)
ordenado = sorted(jogador.items(), key=lambda item: item[1], reverse=True)
sleep(0.5)
print('==Ranking dos jogadores==')
print('-='*12)
for pos, (c, v) in enumerate(ordenado, start=1):
    print(f'{pos}º lugar - O jogador {c} tirou: {v}')
    print('-'*20)
    sleep(0.5)
#from operator import ittemgetter
#sorted(jogo.items(), key=itemgetter(1), reverse=True)