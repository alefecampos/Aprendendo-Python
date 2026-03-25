#ler número, mostrar média, maior valor e menor valor digitado
media = maior = menor = soma = quant = 0
resp = 'S'
while resp in 'Ss':
   # n += n
    n = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    soma += n
    quant += 1
    if quant == 1:
       maior = menor = n
    else:
       if n > maior:
           maior = n
       if n < menor:
           menor = n
media = soma / quant
print('Você digitou {} números, e a média foi {}'.format(quant, media))
print('O maior número foi {} e o menor foi {}'.format(maior, menor))
  #  n = int(input('Digite um número: '))

