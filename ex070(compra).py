totgasto = mil = barato = prodbarato = 0
while True:
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto: R$ '))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    totgasto += valor
    barato = valor
    prodbarato = produto
    if valor > 1000:
        mil += 1
    if valor < barato:
        barato = produto
    if resp == 'N':
        break
print(f'O total gasto na compra foi {totgasto:.2f}\nTemos {mil} produtos custando mais de R$ 1.000,00 \nO produto mais barato foi {prodbarato} custando R$ {barato:.2f}')
