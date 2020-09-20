n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1 > n2:
    print('{} e maior que {}. '.format(n1, n2))
elif n2 > n1:
    print('{} e maior que {}. '.format(n2, n1))
elif n1 == n2 or n2 == n1:
    print('{} e {} são iguais. '.format(n1, n2))
