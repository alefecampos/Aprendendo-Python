#Velocidade de um carro. Se >80 dizer que foi multado. A multa será de 7$ para cada km acima
v = float(input('Velocidade registrada: '))
if v > 80:
    print('Você foi multado')
    print('Valor da multa R$ {:.2f}'.format((v - 80) * 7))
else:
    print('Dirija com segurança')