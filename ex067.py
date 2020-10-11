while True:
    print('Escolha um numero negativo para encerra! ')
    n = int(input('Qual a tabua q vc quer ver? '))
    print('*' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('*' * 30)
print(f'Numero so licitado invalid {n}')
print('Obrigado por usar o app de tabuada!!!')
