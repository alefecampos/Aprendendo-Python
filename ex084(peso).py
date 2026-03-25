pessoas = list()
dado = list()
mai = men = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'N':
            break
    if continuar in 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'Os mais pesados foram {mai}KG. Peso de', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'Os menores pesos registrados foram de {men}. Peso de', end='')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
