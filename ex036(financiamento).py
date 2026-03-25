# calculando empréstimo
# varíáveis: Valor da casa, salário da pessoa, prazo para pagamento
#condições: parcela não exceder 30% da renda mensal
vc = float(input('Qual o valor da casa? R$ '))
s = float(input('Qual é a sua renda mensal? R$ '))
p = int(input('Qual prazo para pagamento (em anos)? '))
print('Você está avaliando uma casa de \033[1;32mR$ {:.2f}\033[m. Sua renda mensal é de \033[1;36mR$ {:.2f}\033[m, e o prazo para pagamento é de \033[1;36{} meses.' .format(vc, s, (p*12)))

parcelamento = vc / (p * 12)
referencia = (parcelamento * 100) / s
print('A parcela simulada é de \033[1;36mR$ {:.2f}\033[m, que equivale a \033[1;36m{}%\033[m da sua renda declarada.'.format(parcelamento, referencia))
if referencia <= 30.00:
    print('\033[1;32mO empréstimo está aprovado!\033[m')
else:
    print('\033[1;31mNão é possível realizar o empréstimo deste valor, no prazo pretendido.\033[m')