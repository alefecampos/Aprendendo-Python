#cálculo de pagamento: dinheiro 10% desconto, cartão à vista 5% desconto, cartão 2x preço normal, cartão 3x ou mais 20% juros
print('{:=^40}'.format('Lojão do Falso'))
p = float(input('Digite o valor do produto: '))
a1 = int(input('[1]- Em dinheiro ou Pix \n[2]- Crédito à vista \n[3]- Crédito em até 2x \n[4]- Crédito em 3x ou mais\nSelecione a forma de pagamento: '))
if a1 == 1:
    p1 = p - (p * 0.1)
    print('Pagamento em dinheiro. O produto de R$ {:.2f} sai por R$ {:.2f}' .format(p, p1))
elif a1 == 2:
    p2 = p - (p * 0.05)
    print('Pagamento no crédito à vista. Você ganhou 5% de desconto, e o valor de R$ {:.2f} sai por R$ {:.2f}' .format(p, p2))
elif a1 == 3:
    print('Pagamento no cartão em 2x sem juros. Valor a ser pago é {:.2f}' .format(p))
elif a1 == 4:
    p3 = p + (p * 0.2)
    condição = int(input('Selecione em quantas parcelas:'))
    print('Pagamento selecionado com parcelamento de {:.2f} de {}x no cartão'.format(p3 // condição, condição))

