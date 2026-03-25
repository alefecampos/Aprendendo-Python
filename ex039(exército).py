#hora de se alistar

from datetime import date
s = str(input('Selecione seu gênero: m / f - '))
if s == 'm':
    a = int(input('Digite o ano que você nasceu: '))
    b = date.today().year
    c = b - a
    d = -c
    if c < 18:
        print('Ainda não é hora de se alistar no exército. Falta(m) {} ano(s)'.format((d + 18)))
    elif c == 18:
        print('Está na hora de se alistar no exército')
    else:
        print('Você deveria ter se alistado no exército há {} anos' .format(c - 18))
if s == 'f':
    print('O alistamento não é obrigatório para mulheres.')