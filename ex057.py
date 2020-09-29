sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Digite seu SEXO novamente pfv: ')).strip().upper()[0]
print('SEXO {} registrado com sucesso!!!'.format(sexo))
