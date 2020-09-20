km = float(input('Quantos KM vc pecorreu com o carro? '))
d = int(input('Quantos dias vc passou com o carro? '))
vd = d * 60
vkm = km * .15
vt = vd + vkm
print('O valor total de aluguel do veiculo sera:{:.2f}' .format(vt))
