from random import randint
v = 0
while True:
    jogador = int(input('Escolha um numero: '))
    pc = randint(0, 11)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar?[P/I]')).strip().upper()[0]
    print(f'Jogador vc escolheu {jogador} e Computador jogou {pc} e o total foi {total}:')
    if tipo == 'P':
        if total % 2 == 0:
            print('Vc ganhou!')
        else:
            print('Vc perdeu! ')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Vc ganhou!')
        else:
            print('Vc perdeu!')
            break
    print('Vamos jogaro novamente? ')
print(f'Game Over. Vc ganhou {v}!')
