s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c
        cont = cont + 1
print('A soma dos numeros é {}:'.format(s))
print('A qnt de numeros solicitados foi {}.'.format(cont))
