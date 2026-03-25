def fatorial(num, show=True):
    """
    -> Calcula o Fatorial de um número.
    :param num: o número a ser calculado.
    :param show: (opcional) mostra (ou oculta) a conta.
    :return: o valor do fatorial.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    if show:
        print(f'{num}x', end='')
        for c in range(num, 1, -1):
            print(f'{c}x', end='')
        print(f'1 = ', end='')
    return f
help(fatorial)
while True:
    num = int(input('Digite um número para saber seu fatorial: '))
    mostrar = str(input('Deseja ver a conta? [S/N]: ')).strip().upper()[0]
    if mostrar == 'S':
        print(fatorial(num, show=True))
    else:
        print(fatorial(num, show=False))
    cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
    while cont not in 'Sn':
        cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if cont == 'N':
            break
