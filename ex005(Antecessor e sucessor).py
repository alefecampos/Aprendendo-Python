n = int(input('Digite um número: '))
print('Você digitou o número \033[0;31m{}\033[m. Seu antecessor é \033[0;34m{}\033[m, e seu sucessor é \033[0;33m{}\033[m' .format(n, n-1, n+1 ))

#problemas: o n não precisa de parênteses; Foi necessário adicionar a variável int antes do input;