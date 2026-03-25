from random import randint
from time import sleep
palpite = list()
dados = list()
lista = list()
cont = 0
print('-'*30)
print(f'    JOGA NA MEGA SENA     ')
print('-'*30)
jogo = int(input('Quantos jogos você quer jogar? '))
print('-='*3,f'SORTEANDO {jogo} JOGOS', '-='*3)
while cont < jogo:
    for c in range (0, 6):
        palpite = randint(1, 60)
        if dados == 0 or palpite not in dados:
            dados.append(palpite)
            lista.append(dados[:])
            dados.clear()
    lista.sort()
    sleep(0.5)
    print(f'Jogo {cont+1}: {lista}')
    lista.clear()
    cont += 1
print('-'*20)
print(f'< BOA SORTE>')
print('-'*20)
