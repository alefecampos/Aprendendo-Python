while True:
    print('-=-'*13)
    n = int(input('Digite um número para saber sua tabuada: '))
    print('-=-'*13)
    if n < 0:
        break
    for cont in range(1, 11):
        print(f'{n} x {cont} = {n * cont}')

print('Fim da Tabuada')