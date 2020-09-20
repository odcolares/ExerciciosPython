vel = float(input('Qual a velocidade do carro? Km/h'))
if vel > 80:
    multa = (vel-80)
    valor = multa * 7
    print('Voce ultrapassou a velocidade permitida em {} KM/h e o valor da multa será R${:.2f}'.format(multa, valor))
else:
    print('Sua velocidade é de {}Km/h. Dirija com segurança e tenha uma boa viagem:'.format(vel))
