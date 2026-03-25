cadastro = list()
continuar = ''
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    cadastro.append([nome, [nota1, nota2], media])
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'N':
            break
    if continuar in 'N':
            break
print('-=' * 13)
print(f'{"Nº":<4}{"Aluno":<10}{"Média":>10}')
print('-'*26)
for i, a in enumerate(cadastro):
    print(f'{i:<4}{a[0]:<10}  {a[2]:>10}')
while True:
    aluno = int(input('Quer visualizar o boletim de qual aluno? '))
    if aluno == 999:
        print('PROGRAMA ENCERRADO')
        break
    if aluno <= len(cadastro) - 1:
        print(f'O aluno {cadastro[aluno][0]} tirou {cadastro[aluno][1]} e {cadastro[aluno][2]}')
