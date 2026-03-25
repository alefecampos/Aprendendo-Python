from time import sleep
def contador(i, f, p):
    print('~'*30)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contando de {i} até {f} de {p} em {p}')
    if i < f:
        for c in range(i, f + 1, p):
            sleep(0.5)
            print(f'{c} ', end='')
    elif i > f:

        a = p * -1
        for c in range(i, f + 1, a):
            sleep(0.5)
            print(f'{c} ', end='')
    print()
    sleep(0.5)
    print('FIM!')
    print('~' * 30)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
contador(i = int(input('Qual o valor inicial? ')), f = int(input('Qual o valor final? ')), p = int(input('Qual o passo? ')))
