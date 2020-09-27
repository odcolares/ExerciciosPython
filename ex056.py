media = 0
somaidade = 0
maioridade = 0
nomevelho = 0
totmulher20 = 0
for pessoa in range(1, 5):
    nome = str(input('Digite seu nome: ')).strip().upper()
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual o sexo: M ou F? ')).upper()
    somaidade += idade
    media = somaidade / 4
    if pessoa == 1 and sexo in 'Mn':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 21:
        totmulher20 += 1

print('A medo do grupo em idade é {}:'.format(media))
print('O {} mais velhor tem {} anos.' .format(nomevelho, idade))
print('Sao {} mulheres menores de 20 anos'.format(totmulher20))
    #print('\033[32m{}\033[m tem \033[32m{} anos\033[m e é do sexo \033[32m{}\033[m'.format(nome, idade, sexo))