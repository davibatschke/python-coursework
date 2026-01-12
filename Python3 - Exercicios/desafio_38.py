# DESAFIO 38 do Curso de Python:
# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

print('\nAnalisando os Numeros...')
if num1 > num2:
    print(f'O Primeiro valor é Maior!')
elif num1 < num2:
    print(f'O Segundo valor é Maior!')
else:
    print('Os Dois valores sao Iguais!')