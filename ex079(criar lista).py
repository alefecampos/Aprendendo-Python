lista = list()
while True:
    valor = (int(input('Digite um valor: ')))
    if valor in lista:
        print('Valor duplicado, impossível adicionar')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    resp = (str(input('Quer continuar? [S/N] '))).strip().upper()[0]
    while resp not in 'SN':
        print('Opção inválida')
        resp = (str(input('Quer continuar? [S/N] '))).strip().upper()[0]
    if resp in 'N':
        break
lista.sort()
print(f'-='* 30)
print(f'Você adicionou os valores {lista}')
print(f'-='* 30)
