f = str(input('Funcionário: '))
n = float(input('Salário atual: '))
print(f'\033[1;4;36m{f}\033[m recebeu um aumento de 15% e seu novo salário é \033[1;4;32mR$ {n+(n*0.15):.2f}\033[m')
