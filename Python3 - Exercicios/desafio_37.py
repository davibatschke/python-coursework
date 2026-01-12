# DESAFIO 37 do Curso de Python:
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um Numero Inteiro: '))

print('[ 1 ] Converter para Binario\n[ 2 ] Converter para Octal\n[ 3 ] Converter para Hexadecimal')
escolha = int(input('Escolha uma base de conversao: '))

if escolha == 1:
    print(f'O seu numero ({numero}) convertido em Binario fica: {bin(numero)}')
elif escolha == 2:
    print(f'O seu numero ({numero}) convertido em Octal fica: {oct(numero)}')
elif escolha == 3:
    print(f'O seu numero ({numero}) convertido em Hexadecimal fica: {hex(numero)}')
else:
    print('Parece que voce escolheu uma Opcao Invalida!')