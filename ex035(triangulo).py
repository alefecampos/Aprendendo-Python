#descobrir se 3 retas podem ser um triângulo
print('-='*20)
print('Analisando triângulos')
print('-='*20)
r1 = float(input('Primeiro valor: '))
r2 = float(input('Segundo valor: '))
r3 = float(input('Terceiro valor: '))

if r1 < r2 + r3 and r2 < r3 + r3 and r3 < r1 + r1:
    print('As retas propostas formam um triângulo.')
else:
    print('As retas propostas não formam um triângulo.')
#primeiro eu tinha feito assim por não ter considerado a r3 < ao mesmo tempo. Muito mais trabalhoso.
"""else:
        if r2 < r3 and r3 < r1 + r1:
            print('As retas propostas formam um triângulo')
        else:
            print('As retas informadas não formam um triângulo')
else:
                if r3 < r1 and r3 < r2 + r2:
                print('As retas propostas formam um triângulo')
                else:
                print('As retas informadas não formam um triângulo')"""
