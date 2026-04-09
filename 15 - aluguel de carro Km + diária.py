p = int(input('Quantas diárias foram consumidas? '))
d = float(input('Quantos kilômetros foram percorridos? '))

valor = (p*60)+(d*0.15)
print(f'Foram consumidas {p} diárias e percorrida a distância de {d} km. Logo, o valor a ser pago é de R$ {valor:.2f}')
