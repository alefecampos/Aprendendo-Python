soma = n = cont = 0
while True:
    n = int(input('Digite um número (digite 999 para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1
print (f'Foram digitados {cont} números, cuja soma é {soma}')
