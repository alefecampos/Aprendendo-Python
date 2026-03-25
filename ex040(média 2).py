#média com recuperação
aluno = str(input('Digite o nome do aluno: ')).strip()
n1 = float(input('Digite a nota para Português: '))
n2 = float(input('Digite a nota para Matemática: '))
m = (n1 + n2) / 2
print('Sua média foi de {}' .format(m))
if m > 7.0:
    print('Você foi \033[1;32mAPROVADO\033[m. Parabéns!')
elif 7 > m >= 5.0 :
    print('Você está de \033[1;34mRECUPERAÇÃO\033[m.')
else:
    print('você foi \033[1;31mREPROVADO\033[m!')
