tem = float(input('Informe a temperatura atual em C°'))
F = (9 * tem/5) + 32
K = tem + 273.15
print('Temperatura informada em Celsius é {:.2f} C°. Sua conversão para Fahrenheit é {:.2f} F° e por fim em Kelvin será {:.2f}: '.format(tem, F, K))
