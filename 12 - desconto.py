p = str(input('Produto: '))
n = float(input('Digite o preço do produto: '))
print(f'O valor de \033[1;4;33m{p}\033[m é \033[1;4;32mR$ {n:.2f}\033[m em até 12x ou \033[1;4;31mR$ {n-(n*0.05):.2f}\033[m para pagamento à vista')
