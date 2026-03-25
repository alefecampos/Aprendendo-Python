print('-='*8)
print('  TABUADA 2.0  ')
print('-='*8)

n = int(input('Digite um número para saber sua tabuada: '))

for c in range(0, 10 +1):
    print('{} * {} = {}'.format(n, c, n * c))