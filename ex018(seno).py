import math
a = float(input('digite o ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print('Para o ângulo {}, o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(a, s, c, t))
