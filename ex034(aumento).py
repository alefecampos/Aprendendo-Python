#calcular aumento: salário > 1250 = 10%; salário =< 1250 = 15%
s = float(input('Qual o seu salário atualmente? '))
if s <= 1250.00:
    print('Seu salário passa a ser de R$ {:.2f}' .format(s + (s * 0.1)))
else:print('Seu salário passa a ser de R$ {:.2f}' .format(s + (s * 0.15)))
