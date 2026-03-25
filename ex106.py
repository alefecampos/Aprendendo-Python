def ajuda(com):
    print('\033[7;32m~'*30)
    print('\033[7;32mSISTEMA DE AJUDA PyHELP')
    print('\033[7;32m~'*30)
    print('\033[m')
    print('\033[7;40m')
    help(com)
    print('\033[m')


while True:
    ajuda(str(input('Função ou Biblioteca > ')))
    cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if cont == 'N':
            break
    if cont == 'N':
        print('\033[0;30;43mATÉ LOGO!\033[m')
        break