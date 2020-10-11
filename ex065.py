resp = 'S'
media = soma = qtd = 0
while resp in 'S':
    num = int(input('Digite um valor: '))
    soma += num
    qtd += 1
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? S/N: ')).upper().strip()[0]
media = soma / qtd
print(f'Qtd de numeros é {qtd} e a media entre eles {media}')
print(f'O maior numero foi {maior} e o menor foi {menor}')

