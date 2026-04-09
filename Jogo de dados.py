from random import randint
from time import sleep


dado1 = randint(1,6)
dado2 = randint(1,6)
print('-='*8)
print('Jogando dados...')
print('-='*8)
sleep(1)
sleep(1)
print(f'Você obteve \033[1;4;30;47m{dado1}\033[m e \033[1;4;30;47m{dado2}\033[m')
