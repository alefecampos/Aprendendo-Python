soma = 0
cont = 0
for c in range(3, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores múltiplos de 3 compreendidos entre 1 e 500 é {}'.format(cont, soma))
