palavras = ('APRENDER', 'PROGRAMAR', 'LINGUGAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
            'MERCADO', 'PROGRAMADOR', 'FUTURO')
vogais = ('A', 'E', 'I', 'O', 'U')
#print(palavras)
for c in palavras:
    print(f'\nna palavra {c.upper()} temos as vogais')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')