# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

s = str(input('Digite: ')).strip()[0]

while s not in 'MmFf':
    s = str(input('Valor Invalido! Digite novamente: ')).strip()[0]

print('cabou')