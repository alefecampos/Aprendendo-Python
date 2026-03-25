def maior(*num):
    print('-='*20)
    print('Analisando os valores informados...')
    if len(num) == 0:
        print(f'Analisando 0')
        print(f'Foram informados 0 valores')
        print(f'O maior número informado foi 0.')
    else:
        print(f'Analisando {num}')
        print(f'Foram informados {len(num)} valores')
        m = max(num)
        print(f'O maior número informado foi {m}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(6, 1)
maior()


