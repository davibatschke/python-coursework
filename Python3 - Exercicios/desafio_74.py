# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados 
# e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros_aleatorios = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Esses foram os cinco números aleatórios gerados: {numeros_aleatorios}')
print(f'O número com maior valor é: {max(numeros_aleatorios)}')
print(f'O número com menor valor é: {min(numeros_aleatorios)}')

# MAX - Método do Python que possibilita encontrar o maior valor
# MIN - Método do Python que possibilita encontrar o menor valor
# Ambos servem para Tuplas e outros tipos de variáveis