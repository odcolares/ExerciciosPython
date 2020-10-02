print('Gerando um PA com laço WHILE no PYTHON....')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end='')
    termo += razao
    cont += 1
print('Fim da PA.')
