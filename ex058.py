from random import randint
pc = randint(0, 10)
print('Digite um numero para tentar advinha o numero que eu escolhi: ')
acertou = False
tentativa = 0
while not acertou:
    jg = int(input('Qual seu palpite? '))
    tentativa += 1
    if jg == pc:
        acertou = True
    else:
       if jg < pc:
           print('Mais...Tente outra vez.')
       else:
           print('MEnos...tente outra vez')
print('Acertou! Com {} tentativas.'.format(tentativa))
