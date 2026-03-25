n = int(input('Digite um número para saber sua tabuada: '))
print('-'*12)
print('A tabuada de \033[1;31m{}\033[m é: \n \033[1;4;33m1x{:2}= {:2} \n 2x{:2}= {:2} \n 3x{:2}= {:2} \n 4x{:2}= {:2} \n 5x{:2}= {:2} \n 6x{:2}= '
      '{:2} \n 7x{:2}= {} \n 8x{:2}= {:2} \n 9x{:2}= {:2} \n 10x{}= {}\033[m' .format(n, n, n*1, n, n*2, n, n*3, n, n*4, n,
                                                                                n*5, n, n*6, n, n*7, n, n*8, n, n*9,
                                                                                n, n*10))
print('-'*12)