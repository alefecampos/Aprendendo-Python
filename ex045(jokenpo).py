import random
from time import sleep
print('-='*10)
print('Vamos jogar jokenpo')
print('-='*10)

p = ['pedra' , 'papel' , 'tesoura']
a = random.choice(p)
#print(a)
b = int(input(' 1- pedra\n 2- papel\n 3- tesoura\n Escolha pedra, papel ou tesoura: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

if a == 'pedra' and b == 1 or a == 'papel' and b == 2 or a == 'tesoura' and b == 3:
    print('EMPATE')
elif a == 'pedra' and b == 2 or a == 'papel' and b == 3 or a == 'tesoura' and b == 1:
    print('Eu escolhi {}. Você ganhou!' .format(a))
elif a == 'pedra' and b == 3 or a == 'papel' and b == 1 or a == 'tesoura' and b == 2:
    print('Eu escolhi {}. Você perdeu' .format(a))
