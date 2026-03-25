
"""minha solução
contador = 0
pa = 0
r = 0
n10 = pa
#n10 = a + (10 - 1) * r
pa = int(input('Digite um número: '))
r = int(input('Digite a razão da P.A.: '))

while contador < 10:
    pa += n10 + r
    contador += 1
    print(pa - r, end='->')
print('FIM')"""

#solução do professor:

print('-=-'*5)
print('Gerador de PA')
print('-=-'*5)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da P.A.: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' ->')
    termo += razão
    cont += 1
print('FIM')
