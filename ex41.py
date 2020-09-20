print('Calculo da media do aluno')
n1 = float(input('Digite a 1 nota: '))
n2 = float(input('Digite a 2 nota: '))
media = (n1+n2) / 2
if media < 5:
    print('A luno \033[1;31mreprovado\033[m com medida {:.1f}. '.format(media))
elif 7 > media > 5:
    print('Aluno em \033[1;33mrecuperação\033[m com a nota {:.1f}. '.format(media))
else:
    print('Aluno \033[1:32mprovado\033[m com media de {:.1f}. '.format(media))
