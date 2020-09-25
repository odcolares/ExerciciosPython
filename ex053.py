numero = int(input('Digite um numero: '))
total = 0
for c in range(1, numero+1):
    if numero % c == 0:
        print('\033[32m', end='')
        total += 1 #Faz a contagem dos elementos
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='') #Cria a lista
if total == 2:
    print('\nO numero {} é PRIMO. '.format(numero))
else:
    print('\nO numero {} foi divisivel {} vezes e por isso nao é primo: '.format(numero, total))
