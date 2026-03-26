#input, soma e resultados com formatação de texto
n1 = int( input('Digite um número: '))
n2 = int (input('digite mais um número: '))
s = n1 + n2
# print('a soma entre', n1 , 'e' ,n2 , 'vale' , s) primeira tentativa. Funcionou, mas não é a melhor opção
print(f'a soma entre \033[1;32m{n1}\033[m e \033[1;32m{n2}\033[m vale \033[1;30;42m{s}\033[m .')
