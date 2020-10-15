print('=' * 30)
print('{:^30}'.format('Banco OPC'))
print('=' * 30)
valor = int(input('Qual o valor que vc deseja sacar? R$'))
total = valor
ced = 200
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'{totced} cedulas de R${ced}')
        if ced == 200:
            ced = 100
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Obrigado por usar o Banco OPC, Volte sempre !!!')
print('=' * 30)

