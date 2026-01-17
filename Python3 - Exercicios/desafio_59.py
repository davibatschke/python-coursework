# Crie um programa que leia dois valores e mostre um menu na tela: somar, multiplicar, maior, novos numeros, sair do programa.
# Seu programa deverá realizar a operação solicitada em cada caso.

import time

numero1 = int(input('Digite um valor: '))
numero2 = int(input('Digite outro valor: '))
escolha = 0

while escolha != 5:
    time.sleep(1)

    print('''
[ 1 ] Somar valores
[ 2 ] Multiplicar valores
[ 3 ] Mostrar valor maior
[ 4 ] Digitar outros valores
[ 5 ] Sair do programa''')
    escolha = int(input('> O que deseja fazer? '))

    if escolha == 1:
        print('A soma entre os Valores:')
        print(f'{numero1} + {numero2} = {numero1 + numero2}')
        print('-' * 25)
    elif escolha == 2:
        print('Multiplicando os Valores:')
        print(f'{numero1} x {numero2} = {numero1 * numero2}')
        print('-' * 25)
    elif escolha == 3:
        if numero1 > numero2:
            print('O Maior Valor entre eles:')
            print(f'{numero1} maior que {numero2}.')
            print('-' * 25)
        elif numero2 > numero1:
            print('O Maior Valor entre eles:')
            print(f'{numero2} maior que {numero1}.')
            print('-' * 25)
        else:
            print('O Maior Valor entre eles:')
            print(f'{numero1} eh igual a {numero2}.')
            print('-' * 25)
    elif escolha == 4:
        numero1 = int(input('Digite um valor: '))
        numero2 = int(input('Digite outro valor: '))
    elif escolha == 5:
        print('Encerrando o sistema...')
        break
    else:
        print(f'Parece que digitou: {escolha}')
        print('Tente novamente.')
        print('-' * 25)