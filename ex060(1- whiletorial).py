#solução inicial do professor
"""from math import factorial
n = int(input('Digite um número para saber o seu fatorial'))
f = factorial(n)
print('O fatorial de {} é {}'.format(n,f))"""





#minha solução:
n = int(input('Digite um número para saber o resultado de seu fatorial: '))
f = 1
c = n
print('Calculando o fatorial de {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ' , end='')

    f *= c
    c -= 1
print('{}'.format(f))