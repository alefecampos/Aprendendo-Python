f = str(input('Funcionário: '))
n = float(input('Salário atual: '))
print('\033[1;4;36m{}\033[m recebeu um aumento de 15% e seu novo salário é \033[1;4;32mR$ {:.2f}\033[m' .format(f, n+(n*0.15)))
