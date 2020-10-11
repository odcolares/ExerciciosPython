n = cont = s = 0
while n != 999:
    n = int(input('Digite um numero. Aperte 999 para finalizar: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'O total de numeros foi {cont} e a sua soma é {s}')
