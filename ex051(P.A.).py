a = int(input('Digite um número: '))
r = int(input('Razão: '))
n10 = a + (10 - 1) * r

for c in range (a, n10 + r, r):
    print(c, end= ' -> ')
print('FIM')