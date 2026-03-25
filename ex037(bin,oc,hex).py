#converter para binário, octal e hexadecimal
print('-='*20)
print('Conversor de bases numéricas')
print('-='*20)
numero = int(input('Digite um número inteiro: '))
print("""Escolha uma das bases para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal""")
opção = int(input('Digite sua opção'))

if opção == 1:
    print('O número {} em binário é {}' .format(numero, bin(numero)[2:]))
elif opção == 2:
    print('O número {} em octal é {}' .format(numero, oct(numero)[2:]))
elif opção == 3:
    print('O número {} em hexadecimal é {}'.format(numero, hex(numero)[2]))
else:
    print('opção inválida')
