frase = str(input('Digite sua frase: ')).lower().strip()

print('A letra "a" aparece {} vezes' .format(frase.count('a')))
print('A letra "a" aparece pela primeira vez em {}' .format(frase.find('a')+1))
print('A letra "a" aparece pela última vez em {}' .format(frase.rfind('a')+1))
