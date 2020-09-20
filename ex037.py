import time
print('Bem vindo...Vamos financiar a sua casa agora!')
time.sleep(2)
valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salario atual? '))
mes = int(input('Em qnt meses vc quer financiar a casa? '))
prestacao = valor / mes
if prestacao > (30 * salario) / 100:
    print('\033[4;31mInfelizmente seu financiamento foi negado\033[m! Vc ultrapassou seu comprometimento salarial em'
          '30%.')
else:
    print('\033[4;32mParabens!!!\033[m Seu financiamento foi aprovado com as seguintes condicoes: ')
    print('Valor da casa R$ {}, tempo de financiamento {} meses e prestação R$ {:.2f}'.format(valor, mes, prestacao))
