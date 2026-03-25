print('\033[1;36m-='*9 )
print('\033[1;36mCalculando seu IMC')
print('\033[1;36m-=\033[m'*9)

altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))

imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está com o peso abaixo do esperado. Procure orientação médica.')
elif imc >= 18.5 and imc <= 25:
    print('Você está no seu peso ideal. Parabens!')
elif imc > 25 and imc <= 30:
    print('Você está com sobrepeso. Procure orientação médica.')
elif imc > 30 and imc <= 40:
    print('Você está com Obesidade Grau I. Procure orientação médica.')
elif imc > 40:
    print('Você está com Obesidade Mórbida. Procure orientação médica urgentemente.')