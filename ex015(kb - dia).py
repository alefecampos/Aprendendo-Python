p = int(input('Quantas diárias foram consumidas? '))
d = float(input('Quantos kilômetros foram percorridos? '))

valor = (p*60)+(d*0.15)
print('Foram consumidas {} diárias e percorrida a distância de {} km. Logo, o valor a ser pago é de R$ {:.2f}' .format(p, d, valor))
