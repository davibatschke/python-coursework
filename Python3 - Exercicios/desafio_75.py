# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num1 = int(input('Digite um Valor: '))
num2 = int(input('Digite outro Valor: '))
num3 = int(input('Digite outro Valor: '))
num4 = int(input('Digite outro Valor: '))
tupla_numeros = (num1, num2, num3, num4)

print(f'\nOs valores que foram digitados: {tupla_numeros}')
print(f'O número Nove (9) apareceu: {tupla_numeros.count(9)} vezes.')

if 3 in tupla_numeros:
    print(f'O número Três (3) apareceu na: {tupla_numeros.index(3) + 1} Posição.')
else:
    print(f'O número Três (3) não apareceu em nenhuma posição.')

print(f'Os valores digitados que são pares: ', end='')
for num in tupla_numeros:
    if num % 2 == 0:
        print(num, end=' ')