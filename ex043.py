print('Não fique constragido:....')
peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('\033[1;33mVc esta abaixo do IMC valor padrao {:.2f}. '.format(imc))
elif 18.5 <= imc < 25:
    print('\033[1;32mPeso ideial seu IMC esta em {:.2f}, PARABENS!!!'.format(imc))
elif 25 <= imc < 30:
    print('\033[1;33mSobre Peso, seu IMC esta em {:.2f}'.format(imc))
elif 30 <= imc < 40:
    print('\033[1;31mObesidade seu IMC esta em {:.2f}'.format(imc))
else:
    print("\033[1;35mVc esta em Obsidade Morbida seu IMC esta em{:.2f}, CUIDADO!. ".format(imc))
