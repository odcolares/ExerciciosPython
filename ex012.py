p = float(input('Qual o valor do produto? '))
des = (((5 * p) / 100) - p) * -1
#pdes = p - des
print('O produto com valor de R${} com a aplicação de 5% de desconto passa a ser R${:.2f}' .format(p, des))
