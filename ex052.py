from time import sleep
print('\033[32mMostre o primeiro termo e a razao de uma PA:\033[m ')
primeiro = int(input('Digite o 1 termo: '))
razao = int(input('Digite a razao: '))
print('Vamos calcular!')
decimo = primeiro + (11 - 1) * razao
for c in range(primeiro, decimo, razao):
    sleep(.5)
    print('{:2}...'.format(c, end='* '))
print('\033[31mACABOU!!!!')
