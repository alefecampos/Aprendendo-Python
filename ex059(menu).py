from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
soma = [1]
multiplicar = [2]
maior = [3]
voltar = [4]
sair = [5]

maior = 0

print('Você inseriu os valores {} e {}. Escolha uma das opções abaixo: '.format(n1, n2))


while opcao != 5:
    print("""          [1] somar
          [2] multiplicar
          [3] mostrar o maior valor
          [4] inserir novos números
          [5] sair""")
    opcao = int(input('Digite uma das opções: '))

    if opcao == 1:
        soma = n1 + n2
        print('{} + {} = {}' .format(n1, n2, soma))
    elif opcao == 2:
        multiplicar = n1 * n2
        print('{} x {} = {}' .format(n1, n2, multiplicar))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('O maior número é {}' .format(maior))
        else:
            maior = n2
            print('O maior número é {}' .format(maior))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        n1 = 0
        n2 = 0
    else:
        print('Opção inválida. Tente novamente')
    sleep(2)
print('Fim da operação.')
