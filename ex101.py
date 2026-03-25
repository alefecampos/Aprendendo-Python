
def voto():
    from datetime import date
    ano = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - ano
    print(f'Com {idade} anos ', end='')
    if idade < 18:
        print('não vota')
    elif idade >= 18 and idade < 65:
        print('o voto é OBRIGATÓRIO.')
    else:
        print('o voto é OPCIONAL.')

voto()


