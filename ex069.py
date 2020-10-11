print('CADASTRO DE PESSOAS: ')
print('*' * 20)
maiores = sexo = man = woman = 0
while True:
    idade = int(input('Qual a idade da pessoal: '))
    if idade >= 18:
        maiores += 1
    if woman < 20 and sexo == 'F':
        woman += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo [F/M]: ')).strip().upper()[0]
        if sexo == 'M':
           man += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]....')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Acabou!!! {man}, {maiores}, {woman}')
