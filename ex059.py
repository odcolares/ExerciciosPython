n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('O que vc que fazer com os valores {} e {}? '.format(n1, n2))
opcao = 0
while opcao != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números             
[ 5 ] sair do programa''')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é = {}:'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('O produto entre {} * {} é = {}.'.format(n1, n2, mult))
    elif opcao == 4:
        print('Digite novos numeros: ')
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('O numero maior é {}. '.format(n1))
        else:
            maior = n2
            print('O numero maior é {}'.format(n2))
print('Fim do programa!!!')
