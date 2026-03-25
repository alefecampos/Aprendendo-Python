#distância da viagem calcule o preço da passagem = 0,50 < 200km e 0,45 > 200km
d = float(input('Quantos km sua viagem terá? '))
if d <= 200:
    print('Sua viagem tem {} km e custará R$ {:.2f}'.format(d, d * 0.50))
else:
    print('Sua viagem tem {} km e custará R${:.2f}'.format(d, d * 0.45))
