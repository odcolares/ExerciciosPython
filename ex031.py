dis = float(input('Qual a distancia da viagem? '))
if dis < 200:
    vl1 = (dis * .50)
    print('O valor da passagem sera de R$ {}'.format(vl1))
else:
    vl2 = (dis * .45)
    print('O valor da passagem sera de R$ {}'.format(vl2))

