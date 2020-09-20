from math import radians, sin, cos, tan
ang = float(input('Digite um angulo: '))
s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))
print('O SENO do angulo {} é {:.2f}'.format(ang, s))
print('O COSENO do angulo {} é {:.2f}'.format(ang, c))
print('A TANGENTE do angulo {} é {:.2f}'.format(ang, t))
