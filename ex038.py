numero = int(input('Digite um numero e escolha sua conversao: '))
print('''Escolha uma das opçoes a seguir: 
[1] BINARIO
[2] OCTAL
[3] HEXA''')
escolha = int(input('Sua opção: '))
if escolha == 1:
    print('Vc escolheu \033[1;33m{}\033[m e seu formato em \033[1;31mBinario é {}.'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('Vc escolheu \033[1;33m{}\033[m e seu formato em \033[1;35mOctal é {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('Vc escolheu \033[1;33m{}\033[m e seu formato em  \033[1;36mHexa é {}'. format(numero, hex(numero)[2:]))
else:
    print('Opção invalida...')
