#comparador de números
v1 = int(input('Primeiro número: '))
v2 = int(input('Segundo número: '))

if v1 > v2:
    print('O primeiro valor digitado é {}, e é maior que o segundo valor digitado {}' .format(v1,v2))
elif v1 < v2:
    print('O segundo valor digitado é {} e é maior que o primeiro {}' .format(v2,v1))
else:
    print('Os dois valors são iguais')
