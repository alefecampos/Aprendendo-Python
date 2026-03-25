from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10),
       randint(1, 10), randint(1, 10))
#num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f'Os números sorteados foram: ')
for n in num:
    print(f'{n}|', end=' ')
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')