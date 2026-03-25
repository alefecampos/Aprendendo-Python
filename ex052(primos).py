import math
n = int(input('Digite um número para saber se ele é primo: '))
for c in range(1):
    if n == 1 or 0:
        print('O número {} não é primo' .format(n))
    elif n == 2:
        print('O número {} é primo'.format(n))
    elif n % 2 == 0:
        print('O número {} não é primo'.format(n))
    elif n % math.sqrt (n) != 0:
        print('O número {} é primo'.format(n))
    else:
        print('O número {} não é primo '.format(n))