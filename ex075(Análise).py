num = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')),
       int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')))
print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O primeiro valor 3 aparece na {num.index(3)+1}ª posição')
else:
    print('O número 3 não apareceu na lista')
print(f'Os valores pares foram: ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
