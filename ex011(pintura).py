n1 = float(input('Qual a altura da parede? '))
n2 = float(input('Qual a largura da parede? '))

print('Você vai precisar de \033[1;34;41m{}\033[m litros de tinta para pintar a área de \033[1;34;41m{}m²\033[m' .format((n1*n2)/2 , n1*n2))
