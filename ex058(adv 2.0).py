from random import randint
from time import sleep

p = -1
n = randint(0,10)
palpite = 0
print('-=-'*28)
print('Eu vou pensar em um número. Você vai tentar adivinhar. Use quantos palpites precisar')
print('-=-'*28)
print(n)
#condição que encerra o programa tem que vir primeiro. Senão ele vai exibir a mensagem "falsa" junto com a verdadeira.
while n != p:
    p = int(input('Digite seu palpite: '))
    print('PROCESSANDO...')
    sleep(0.5)
    if n == palpite:
        print('Você acertou!')
        palpite += 1
    elif n != palpite:
        print('Este não é o número que eu pensei. Tente novamente.')
        palpite += 1
print('Parabéns! Você acertou na {}ª tentativa'.format(palpite))

"""Solução do professor:
acertou = False
palpite = 0
while not acertou: 
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez')
        elif jogador > computador:
            print('Menos... tente mais uma vez')
            
print('Acertou com {} palpites'.format(palpite))
    """