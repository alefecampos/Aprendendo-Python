print('-=-'*5)
print('Gerador de PA')
print('-=-'*5)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da P.A.: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo), end=' ->')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos mais você gostaria de visualizar? '))
print('Progressão finalizada com sucesso. Foram exibidos ao todo {} termos.'.format(total))