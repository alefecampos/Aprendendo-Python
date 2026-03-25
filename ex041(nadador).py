from datetime import date
print('-='*25)
print('Bem vindo à Confederação Nacional de Natação - CNN')
print('-='*25)
i = int(input('Para começar, digite seu ano de nascimento: '))
t = date.today().year
a = t - i
if a <= 9:
    print('Você tem {} anos de idade e está inscrito na categoria \033[1;33mMIRIM\033[m'.format(a))
elif a <= 14:
    print('Você tem {} anos de idade e está inscrito na categoria \033[1;32mINFANTIL\033[m'.format(a))
elif a <= 19:
    print('Você tem {} anos de idade e está inscrito na categoria \033[1;35mJUNIOR\033[m'.format(a) )
elif a <= 20:
    print('Você tem {} anos de idade e está inscrito na categoria \033[1;34mSENIOR\033[m'.format(a))
elif a > 25:
    print('Você tem {} anos de idade e está inscrito na categoria \033[1;34mMASTER\033[m'.format(a))
