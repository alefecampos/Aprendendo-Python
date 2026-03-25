lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'S':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'N':
            break
    if continuar in 'N':
        break
print(f'Você digitou {len(lista)} números.')
if 5 in lista:
    print('A lista possui o número 5')
else:
    print('O número 5 não aparece na lista')
lista.sort(reverse=True)
print(f'A lista de valores em ordem decrescente é {lista}')
