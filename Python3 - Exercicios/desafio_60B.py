# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
# Versao com FOR em Python

from math import factorial

numero = int(input('Digite um Valor para calcular o seu Fatorial: '))
print(f'O resultado do Fatorial de {numero}:')

for contagem in range(numero, 0, -1):
    print(f'{contagem}', end='')
    print(f' x ' if contagem > 1 else ' = ', end='')
print(f'{factorial(numero)}')
