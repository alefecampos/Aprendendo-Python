P = str(input('Produto: '))
n = float(input('Digite o preço do produto: '))
print('O valor de \033[1;4;33m{}\033[m é \033[1;4;32mR$ {:.2f}\033[m em até 12x ou \033[1;4;31mR$ {:.2f}\033[m para pagamento à vista' .format(P, n, (n-(n*0.05))))
