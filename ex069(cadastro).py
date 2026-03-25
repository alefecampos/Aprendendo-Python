print('-'*15)
print('Cadastro aberto')
print('-'*15)
sexo = homem = idade = totmaior = mulmenor = 0
while True:
    sexo = ' '
    idade = int(input('Digite a idade: '))
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    cadastro = ' '
    while cadastro not in 'SN':
        cadastro = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if sexo == 'M':
        homem += 1
    if idade > 18:
        totmaior += 1
    if idade <= 18 and sexo in 'Ff':
        mulmenor += 1
    if cadastro == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {totmaior} ')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulmenor} mulheres cadastradas com menos de 18 anos.')
