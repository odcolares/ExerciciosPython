n = int(input('Digite um numero: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('O numero digitado foi {}.'.format(n))
print('Sua unidade é {}' .format(u))
print('Sua dezena é {}'.format(d))
print('Sua Centena é {}' .format(c))
print('Sua Milhar é {}'.format(m))
