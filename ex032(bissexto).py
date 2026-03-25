#ano bissexto
from datetime import date
a = int(input('Digite o ano para saber se é bissexto (digite 0 para o ano atual): '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    # != é o símbolo para diferente; == é o símbolo para igual
    print('O ano {} é bissexto!'.format(a))
else:
    print('O ano {} não é bissexto!'.format(a))


