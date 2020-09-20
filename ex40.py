from datetime import date
data_atual = date.today().year
ano = int(input('Digite o ano de seu nascimento: '))
idade = data_atual - ano
print('Seu ano de dascimento foi {}, vc tem {} anos no ano de {}.'.format(ano, idade, data_atual))
if idade == 18:
    print('Vc nasceu em {} sua idade é de {} no ano de {} esta no periodo de alistamento.'.format(ano, idade, data_atual))
elif idade < 18:
    saldo = idade - 18
    print('Vc nasceu no ano de {} sua idade é de {} anos. Seu alistamento esta previsto para o ano {}.'.format(ano, idade, saldo))
else:
    print('Vc esta atrasado para o alistamento em {}. Apresente-se:' .format(ano))
