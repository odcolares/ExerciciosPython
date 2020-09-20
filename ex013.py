s = float(input('Qual o seu salario atual? R$'))
sa = s + (s * 15 / 100)
print('Seu salario antigo de R${:.2f} foi reajustado em 15% para R${:.2f}' .format(s, sa))
