#Aqui são as firulas!!!
print('SIMULADOR DE CAIXA ELETRÔNICO BANDO OPC')
print('=' * 30)
print('{:^30}'.format('Banco OPC'))
print('=' * 30)

#Solicitando o valor a ser sacado.
valor = int(input('Qual o valor que vc deseja sacar? R$'))

total = valor #total recebendo o valor solicitado pelo cliente
ced = 200   #Variavel iniciando com o maior valor de nota
totced = 0 #Contador de cedulas
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0: #Fiz a tratativa para que nao aparece total "0" cedulas na tela.
            print(f'{totced} cedulas de R${ced}')
        #Aqui começa magica a variavel CED recebendo o menor valor seguinte, para que aja a contagem das cedulas até
        # "Zerar" o saldo solicitado pelo cliente e finalizar o laço com um break.
        if ced == 200:
            ced = 100
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
#Mais firulas para enfeitar kkkkkkkkkk
print('=' * 30)
print('Obrigado por usar o Banco OPC, Volte sempre !!!')
print('=' * 30)

