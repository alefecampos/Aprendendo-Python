times = ('PALMEIRAS', 'SÃO PAULO', 'FLUMINENSE', 'BAHIA', 'CORINTHIANS', 'ATHLETICO_PR', 'BRAGANTINO', 'CHAPECOENSE', 'MIRASSOL', 'CORITIBA', 'FLAMENGO', 'BOTAFOGO', 'GRÊMIO', 'EC_VITORIA', 'ATLÉTICO-MG', 'REMO', 'VASCO_DA_GAMA', 'SANTOS', 'INTERNACIONAL', 'CRUZEIRO')
print('='*30)
print(f'Os 5 primeiros colocados são:')
print('='*30)
for c in range(0, 5):
    print(f'{times[c]} na posição {c+1} ')
print('='*30)
print(f'Os 4 últimos colocados são: ')
# solução do professor: print(f'Os 4 ultimos são {times[-4:]}')
print('='*30)
#assim ficou mais legal
for ultimo in range(16, len(times)):
     print(f'{times[ultimo]} na posição {ultimo+1}')
print('='*30)
print(f'Os times em ordem alfabética são: ' )
print(f' Os times em ordem alfabética é {sorted(times)}')
print('='*30)
print(f'O time da chapecoense está na {times.index('CHAPECOENSE')+1}ª posição' )
print('='*30)