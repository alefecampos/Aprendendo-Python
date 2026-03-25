cadastro = list()
pessoa = dict()
mulheres = []
mediamai = list()
pidade = 0
#recebendo dados
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while pessoa['sexo'] not in 'MmFf':
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    cadastro.append(pessoa.copy())
    pidade += pessoa['idade']
    if pessoa['sexo'] in 'F':
        mulheres.append(pessoa['nome'])
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
        if continuar in 'N':
            break
    if continuar in 'N':
        break
media = pidade / len(cadastro)
for pessoa in cadastro:
    if pessoa["idade"] >= media:
        mediamai.append(pessoa["nome"])
print('-='*15)
print(f'O grupo tem {len(cadastro)} pessoas')
print('-'*30)
print(f'A média de idade do grupo é {media:5.1f}')
print('-'*30)
print(f'As mulheres cadastradas foram {mulheres}.')
print('-'*30)
print(f'Foram encontradas as seguintes pessoas com idade acima de {media}:')
print(f'acima da media {mediamai}', end=' ')
print()

print('-'*30)
print('Lista:')
print(cadastro)
print('-'*30)
print('Dicionários')
print(pessoa)