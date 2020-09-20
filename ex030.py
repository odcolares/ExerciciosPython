from time import sleep
n = int(input('Digite um numero...'))
print('Loading....')
sleep(2)
r = n % 2
if r == 0:
    print('Seu numero {} é par'.format(n))
else:
    print('Seu numero {} é impar'.format(n))
