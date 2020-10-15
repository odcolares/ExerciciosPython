print('=' * 30)
print('{:^30}'.format('Lista de compras!'))
print('=' * 30)
total = deMil = menor = maior = cont = 0
barato = mcaro = ' '
while True:
    produto = str(input('Adicione o item ao seu carrinho: \n'))
    valor = float(input('Qual o valor do item? \nR$'))
    cont += 1
    total += valor
    if valor > 999:
        deMil += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto
    if cont == 1 or valor > maior:
        maior = valor
        mcaro = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer adicionar mais produtos ao carrinho? [S/N] \n')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O valor total das compras foi ${total:.2f}.')
print(f'Tivemos {deMil} protudos acima de $1000 na lista.')
print(f'O item mais caro foi {mcaro} e custou ${maior:.2f}.')
print(f'O item mais barato foi {barato} e custou ${menor:.2f}. ')
print('Compra finalizada, obg e volte sempre!!!.')
