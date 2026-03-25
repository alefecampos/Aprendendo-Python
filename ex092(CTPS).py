#ler nome, ano de nascimento e carteira de trabalho (se carteira de trabalho == 0, encerra o laço e mostra os dados)
#se tiver CTPS, ler ano de contratação e salário tbm, e calcular com quantos anos a pessoa vai se aposentar.
#print nome, idade, CTPS, ano de contratação, salário e idade prevista para aposentadoria.
#aposentadoria == 35 anos de contribuição
from datetime import date
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
cadastro['idade'] = date.today().year - nasc
cadastro['carteira'] = int(input('Carteira de trabalho (se não tiver, digite 0): '))
if cadastro['carteira'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salario'] = int(input('Salário: R$ '))
    cadastro['aposentadoria'] = (cadastro['contratação'] + 35) - nasc
print('-='*15)
print('CADASTRO DO CIDADÃO [CC]')
print('--'*15)
#poderia fazer for k, v in dados.items():
#print(f' - {k} tem o valor {v}')
print(f'O cidadão {cadastro["nome"]} tem {cadastro["idade"]} anos.\n'
      f'CTPS nº {cadastro["carteira"]}')
if cadastro['carteira'] != 0:
    print(f'Registrada primeira contratação em {cadastro["contratação"]}\n'
      f'Salário atual registrado em {cadastro["salario"]}\n'
      f'É prevista a aposentadoria com a idade de {cadastro["aposentadoria"]}\n')
print('-='*15)
print('Fim do cadastro')
print('-='*15)
