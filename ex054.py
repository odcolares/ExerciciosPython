from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {} pessoa: '.format(c)))
    idade = atual - ano
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('O total de pessoas menores de idade sao {}'.format(totalmenor))
print('O total de pessoas maiores de idade sao {}.'.format(totalmaior))
