from datetime import date
data_atual = date.today().year
ano = int(input('Qual o ano de seu nascimento: '))
prova = data_atual - ano
if prova <= 9:
    print('Sua idade é de {} anos. Categoria do atleta é MIRIM. '.format(prova))
elif 10 > prova <= 14:
    print('Sua idade é {} anos e sua categoria será INFANTIL'.format(prova))
elif 15 > prova <=19:
    print('Sua idade é {} anos e sua categoria é JUNIOR.'.format(prova))
elif 20 > prova <=25:
    print('Sua idade é de {} anos e sua categoria será SÊNIOR.'.format(prova))
else:
    print('Sua idade é {} anos e sua categoria é MASSTER.'.format(prova))
