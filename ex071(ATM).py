print('-'*17)
print('Bem vindo ao CEV!')
print('-'*17)

saque = int(input('Qual valor a ser sacado? R$ '))
total = saque
ced = 50
totcedulas = 0
while True:
    if total >= ced:
        total -= ced
        totcedulas += 1
    else:
        if totcedulas > 0:
            print(f'Total de {totcedulas} cédulas de R$ {ced:.2f}')
        if ced == 50:
            ced = 20
            totcedulas = 0
            if totcedulas > 0:
                print(f'Total de {totcedulas} de R$ {ced:.2f}')
        elif ced == 20:
            ced = 10
            totcedulas = 0
            if totcedulas > 0:
                print(f'Total de {totcedulas} de R$ {ced:.2f}')
        elif ced == 10:
            ced = 1
            totcedulas = 0
            if totcedulas > 0:
                print(f'Total de {totcedulas} de R$ {ced:.2f}')
        if total == 0:
            break