cont = n = soma = 0
n = int(input('Entre com o valor desejado ou 999 para dar stop. '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Entre com o valor desejado ou 999 para dar stop. '))
print('Vc digitou {} numeros e a soma é de {}: '.format(cont, soma))

