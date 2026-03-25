#desafio dos triângulos 2. Dizer se é isóceles, equilátero ou escaleno
print('-='*20)
print('Analisando triângulos')
print('-='*20)

r1 = float(input('Primeiro valor: '))
r2 = float(input('Segundo valor: '))
r3 = float(input('Terceiro valor: '))

if r1 < r2 + r3 and r2 < r3 + r3 and r3 < r1 + r1:
    print('As retas propostas formam um triângulo.')
    if r1 == r2 and r1 == r3:
        print('Este é um triângulo EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('Este é um triângulo ESCALENO')
    else:
        print('Este é um triângulo ISÓCELES')
else:
    print('As retas propostas não formam um triângulo')






