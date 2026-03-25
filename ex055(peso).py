maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso lido foi {}Kg e o menor peso digitado foi {}Kg' .format(maior, menor))
