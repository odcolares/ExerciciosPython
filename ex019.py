import random
num1 = str(input('Digite o primeiro aluno'))
num2 = str(input('Digite o segundo aluno'))
num3 = str(input('Digite o terceiro aluno'))
num4 = str(input('Digite o quarto aluno'))
lista = [num1, num2, num3, num4]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))
