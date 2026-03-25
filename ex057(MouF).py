m = f = 0
sexo = 1

while sexo != 'SAIR':
    sexo = str(input('Digite o sexo [M/F]: ')).upper()[0] #o [0] serve pra pegar só a primeira letra digitada
    if sexo == 'Mm':
        m += 1
    elif sexo == 'Ff':
        f += 1
    elif sexo != 'Mm' and sexo != 'Ff':
        print('opção inválida. Tente novamente com M ou F')
print('Você foram computados {} homens e {} mulheres'.format(m, f))

"""solução do professor:
sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
idade = int(input('Digite sua idade: '))
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, digite seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo)"""