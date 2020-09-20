from time import sleep
v1 = float(input('Digite um valor: '))
v2 = float(input('Digite outro valor: '))
v3 = float(input('Digite um terceiro valor: '))
print('Vamos analisar qual o maior e o menor valor: ')
print('Analisando....')
sleep(2)

maior = v1
if v2 > v1 and v3:
    maior = v2
if v3 > v1 and v2:
    maior = v3

menor = v1
if v2 < v1 and v3:
    menor = v2
if v3 < v1 and v2:
    menor = v3
print('O menor {}'.format(menor))
print('O maior {}'.format(maior))

