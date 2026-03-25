lista = []
listapar = []
listaimpar = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    continuar = ' '
    while continuar not in 'S':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'N':
            break
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    if continuar in 'N':
        break
print(f'A lista é {lista}, \nOs números pares são {listapar} \nOs números ímpares são {listaimpar}')