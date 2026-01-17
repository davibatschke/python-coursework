# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido 
# quando o número solicitado for negativo.

valor = 0

while True:
    valor = int(input('Digite um Valor: '))

    if valor < 0:
        print('Número Negativo!')
        break

    for i in range(1, 11):
        print(f'{valor} x {i} = {valor * i}')