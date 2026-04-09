n = str(input('Digite o nome do aluno: '))
n1 = float(input('Qual foi a nota em português?'))
n2 = float(input('Qual foi a nota em matemática?'))
m = (n1 + n2)/2
print(f'\033[14;33m{n}\033[m tirou \033[1;35m{n1:.1f}\033[m em português, \033[1;35m{n2:.1f}\033[m em matemática, e teve a média de \033[1;35m{m:.1f}\033[m')
if m >= 6.0:
    print('\033[0;32mSua média foi boa. PARABÉNS\033[m')
else:
    print('\033[0;31mSua média foi ruim. ESTUDE MAIS!\033[m')
#dificuldade - faltou os parênteses na função de média, de forma que o programa resolvia primero a divisão.
