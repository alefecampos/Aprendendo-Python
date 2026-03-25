def leiaint(a):
    while True:
        num = input('Digite um número: ')
        try:
            n = int(num)
            return n
        except ValueError:
            print('ERRO! Digite um número inteiro válido')

numero = leiaint('Digite um número: ')
print(f'Você digitou o número {numero}')
