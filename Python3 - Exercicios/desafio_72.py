# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado 
# (entre 0 e 20) e mostrá-lo por extenso.

numeros_por_extense = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

escolha_usuario = int(input('Digite um número (0-20): '))

while True:
    if escolha_usuario > 20 or escolha_usuario < 0:
        print(f'O número escolhido precisa estar entre 0 e 20.')
        escolha_usuario = int(input('Tente novamente. Digite um número: '))

    else:
        print(f'Você digitou o número: {numeros_por_extense[escolha_usuario]}.')
        break