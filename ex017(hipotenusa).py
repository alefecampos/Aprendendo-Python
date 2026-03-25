#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

import math

#método matemático
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))

#calculando a hipotenusa
h = float((co ** 2) + (ca ** 2))
print('o triângulo retângulo cujo cateto oposto é {} e cateto adjacente é {}, tem a hipotenusa {}. ' .format(co, ca, math.sqrt(h)))

#método modular

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente:'))
hi = math.hypot(co, ca)
print('A hipotenusa mede {}' .format(hi))