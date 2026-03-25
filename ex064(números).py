print('-=-'*15)
print('Leitor e somatório. Digite 999 para encerrar')
print('-=-'*15)
n = nt = st = 0

while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        nt += 1
        st += n
        #if n != 999:
        #print('Você digitou o número {}'.format(n))
    else:
        print('Você digitou {} números. A soma dos valores digitados foi {}'.format(nt, st))
print('Fim')