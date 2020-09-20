valor = float(input('Qual o valor do produto a ser pago? '))
print('''Escolha a forma de pagamento:
[1] A vista dinheiro/cheque: 10% de desconto.
[2] à vista no cartão: 5% de desconto.
[3] em até 2x no cartão: preço formal.
[4] 3x ou mais no cartão: 20% de juros.''')

opcao = int(input('Escolha a forma de pagamento: '))
if opcao == 1:
    total1 = valor - (valor * 10 /100)
    print('Valor a ser pago será: {}'.format(total1))
elif opcao == 2:
    total2 = valor - (valor * 5 /100)
    print('Valor a ser pago será: {}'.format(total2))
elif opcao == 3:
    print('Valor a ser pago será: {}'.format(valor))
else:
    total3 = valor + (valor * 20 /100)
    print('O valor total a ser pago é de R${}.'.format(total3))
