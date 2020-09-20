import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hp = math.hypot(co, ca)
print('O valor da hipotenusa é {:.1f}' .format(hp))
