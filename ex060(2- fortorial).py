
n = int(input('Digite um número para saber o resultado de seu fatorial: '))
f = 1
c = n
print('Calculando o fatorial de {}! = '.format(n), end='')
for c in range (n, 1, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ' , end='')
    f *= c
    c -= 1
print('{}'.format(f))