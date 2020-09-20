salario = float(input('Qual o seu salario? '))
if salario <= 1250:
    sn = salario + ((15 * salario) / 100)
else:
    sn = salario + ((10 * salario) / 100)
print('Seu novo salario é de {}: '.format(sn))

