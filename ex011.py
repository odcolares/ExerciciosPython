L = float(input('Qual a largura de sua parede? '))
A = float(input('Qual a altura de sua parede? '))
area = L * A
p = (area * 1) / 2
print('A sua parede tem a area de {:.2f}' .format(area), 'm²')
print('Para pintar essa metragem de {:.2f}m² voce ira precisar de {:.2f}L' .format(area, p))

