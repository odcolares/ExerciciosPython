num = int(input('Digite um numero: '))
for c in range(1, 11):
    if c % 2 == 0:
        print('{} * {:2} = {}'.format(num, c, num * c))

