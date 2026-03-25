lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = maior = col3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite um valor para a posição {[l]}, {[c]}: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{lista[l][c]:^5}', end='')
        if lista[l][c] % 2 == 0:
            par += lista[l][c]
    print()
for l in range(0, 3):
    col3 += lista[l][2]
for c in range(0, 3):
    if c == 0:
        maior = lista[1][c]
    elif lista[1][c] > maior:
        maior = lista[1][c]
print(f'A soma dos valores da terceira coluna é {col3}.')
print(f'O maior valor da segunda linha é {maior}')
print(f'A soma dos números pares é {par}')