from random import randint
print('-=-'*8)
print('Vamos jogar PAR OU IMPAR')
print('-=-'*8)
cont = 0
while True:
    computador = randint(0, 10)
    #print(computador)
    n = int(input('Escolha um número: '))
    total = computador + n
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {n} e eu escolhi {computador}. O total foi {total}... ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if pi == 'P':
        if total % 2 == 0:
            print('Você venceu.')
            cont += 1
        else:
            print('Você perdeu.')
            break
    elif pi == 'I':
        if total % 2 == 1:
            print('Você venceu')
            cont += 1
        else:
            print('Você perdeu.')
            break
    print('-=-'*8)
    print('Vamos jogar novamente...')
    print('-=-' * 8)
print(f'GAME OVER. Você venceu {cont} vezes.')
