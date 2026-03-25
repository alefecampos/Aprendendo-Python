#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep

número = randint(0, 5)
#print(número)
print('-=-'*20)
print('Vou pensar em um número entre 0 a 5. Você consegue adivinhar qual será?')
print('-=-'*20)
palpite = (int(input('Digite seu palpite: ')))
print('Pensando...')
sleep(2)

print('Você escolheu o número {}. O número sorteado foi {}'.format(palpite, número))

if número == palpite:
    print('parabéns você é um adivinho!')
else:
    print('Tente outra vez')