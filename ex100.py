from random import randint
from time import sleep


numeros = []
def sorteio(numero):
    print('Sorteando 5 valores da lista: ')
    for c in range(0, 5):
        n = randint(1, 10)
        sleep(0.5)
        print(f'{n}', end=' ')
        numeros.append(n)
    sleep(0.5)
    print()


def somapar(numero):
    soma = 0
    for c, v in enumerate(numero):
        if v % 2 == 0:
            soma += v
            if soma == 0:
                print('SÓ TEM NÚMERO ÍMPAR AQUI? É ISSO MESMO!')
    print(f'A soma dos números pares em {numero} é: {soma}')

    
