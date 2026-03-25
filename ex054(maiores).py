from datetime import date
maiores = 0
menores = 0
for ano in range (7):
    ano = int(input('Digite o ano de nascimento: '))
    t = date.today().year
    i = t - ano
    if i > 21:
        #print('Esta pessoa já é maior de idade')
        maiores += 1
    else:
       # print('Esta pessoa ainda não atingiu a maioridade')
        menores += 1
print('Da lista digitada, {} são maiores de idade, e {} são menores de idade' .format(maiores, menores))
