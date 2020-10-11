print('GERENCIADOR DE PAGAMENTOS')
print('*' * 30)
valor = float(input('Qual o valor do produto a ser pago? '))
print('''Escolha a forma de pagamento:
[1] A vista dinheiro/cheque: 10% de desconto.
[2] à vista no cartão: 5% de desconto.
[3] em até 2x no cartão: preço formal.
[4] 3x ou mais no cartão: 20% de juros.''')
print('*' * 30)

opcao = int(input('Escolha a forma de pagamento: '))
if opcao == 1:
    total1 = valor - (valor * 10 /100)
    print('Pagamento a Vista c/ dinheiro!')
    print(f'Valor a ser pago será: R${total1}')
elif opcao == 2:
    total2 = valor - (valor * 5 /100)
    print('Pagamento a Vista no debito!')
    print(f'Valor a ser pago será: R${total2}')
elif opcao == 3:
    print('Pagamento parcelado ate 2x. Preço sem desconto!')
    print(f'Valor a ser pago será: R${valor}')
else:
    print('Pagamento parcela acima de 2x acrescimo de 20% no valor da compra!')
    total3 = valor + (valor * 20 /100)
    print(f'O valor total a ser pago é de R${total3}.')
