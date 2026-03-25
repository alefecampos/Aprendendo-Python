nome = str(input('Digite seu nome completo: ')).strip()
#função .strip remove os espaços inúteis
print('Analisando seu nome...')
print('Seu nome em maíusculas é: {}' .format(nome.upper()))
print('Seu nome em minúsculas é: {}' .format(nome.lower()))
print('Seu nome tem {} letras' .format(len(nome) - nome.count(' ')))
#função menos .count ' ' espaço
dividido = (nome.split())
#print('Seu primeiro nome tem: {}' .format(len(dividido[0]))) fiz assim sozinho;
print('Seu primeiro nome é {} e tem {} letras' .format(dividido[0], len(dividido[0])))