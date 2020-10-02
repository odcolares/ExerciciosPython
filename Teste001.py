'''n = int(input('Digite um nota: '))
while n < 0 or n > 10:
   n = int(input('Tente novamente. Qual a nota? '))
print('Nota {} foi registrada corrta!'.format(n))'''

'''nome = input('Digite seu nome? ')
senha = input('Digite sua senha? ')
while senha == nome:
    print('Erro no cadastro nome e senha iguais. Tente novamente. ')
    senha = input('Senha: ')
print('Cadastro realizado com sucesso!!!')'''

'''sexo = str(input('Informe seu sexo M ou F')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Sexo invalido, tente novamente: '))
print('Sexo {} foi registrado com sucesso!'.format(sexo))'''

nome = str(input('Digite seu nome? ')).strip().upper()
idade = int(input('Quantos anos? '))
salario = float(input('Digite seu salario: '))
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
print('Informe seu estado civil: ')
es = str(input('''[1] Solteiro
[2] Casado
[3] Viuvo
[4] Divorciado: ''')).strip().upper()
len(nome)
while len(nome) <= 3:
    print('Nome Invalido. Tente novamente!')
    nome = str(input('Digite novamente: '))
while idade < 18 or idade > 150:
    print('Idade incorreta! Tente novamente: ')
    idade = int(input('Digite sua idade: '))
while salario < 1:
    print('Salario tem q ser maior que 0. Tente novamente:  ')
    salario = float(input('Digite seu salario: '))
while sexo not in 'MF':
    sexo = str(input('Digite seu SEXO novamente pfv: ')).strip().upper()[0]
while es not in '1234':
    es = str(input('Estado civel invalido. Digite novamente: ')).strip().upper()
print('Ola {}!'.format(nome))
print('Sua idade {} anos foi registrada com sucesso.'.format(idade))
print('Salario de R${:.2f} foi registrado com sucesso!!!'.format(salario))
print('SEXO {} registrado com sucesso!!!'.format(sexo))
print('Estado civil {} registrado com sucesso!'.format(es))

