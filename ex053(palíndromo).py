frase = 0
frase = str(input('Digite uma frase para saber se é um palíndromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('A frase {} é um palíndromo' .format(junto))
else:
    print('a frase não é um palíndromo')

#fiz sozinho assim. Fatiamento fica mais simples, mas o objetivo do exercício era usar o for in range
"""if frase == frase[::-1]:
    print('Esta frase é um palíndromo')
else:
    print('Esta frase não é um palíndromo')"""
