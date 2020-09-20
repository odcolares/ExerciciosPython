from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opçoes:
0 - Pedra
1 - Papel
2 - Tesoura''')
jogador = int(input('Qual a sua jogada? '))
print('-=' * 11)
print('Jogador jogou {}'.format(itens[jogador]))
print('Computador jogou {}'.format(itens[computador]))
print('-=' * 11)
if computador == 0: #computador joga Pedra.
    if jogador == 0:
        print('Jagada empatada:')
    elif jogador == 1:
        print('Vc ganhou!!!')
    elif jogador == 2:
        print('Vc perdeu!!!')
    else:
        print('Jogada invalida!!!')
elif computador == 1: #computador jogou Papel.
    if jogador == 0:
        print('Vc ganhou!!!')
    elif jogador == 1:
        print('Vc empatou...')
    elif jogador == 2:
        print('Vc perdeu')
    else:
        print('Jogada invalida!!!')
if computador == 2: #computador jogou tesoura.
    if jogador == 0:
        print('Vc perdeu!!!')
    elif jogador == 1:
        print('Vc ganhou!')
    elif jogador == 2:
        print('Vc empatou')
