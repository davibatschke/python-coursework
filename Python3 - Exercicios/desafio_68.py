# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas 
# que ele conquistou no final do jogo.

import random

player_numero = bot_numero = resultado_final = contador_vitorias = 0
player_escolha = ''

print('====================================')
print('====[ Par ou ímpar com Python! ]====')
print('====================================')

while True:
    player_numero = int(input('Digite um Valor: '))
    player_escolha = str(input('Escolha entre par ou ímpar [P/I]: ')).strip()[0]
    bot_numero = random.randint(1, 10)
    resultado_final = (player_numero + bot_numero) % 2

    if resultado_final == 0 and player_escolha in 'Pp':
        print(f'\nBoa! Voce ganhou, eu tinha escolhido {bot_numero}.')
        contador_vitorias += 1
        print('====================================')

    elif resultado_final == 1 and player_escolha in 'Ii':
        print(f'\nBoa! Voce ganhou, eu tinha escolhido {bot_numero}.')
        contador_vitorias += 1
        print('====================================')

    else:
        break

print('\n====================================')
print('===========[ GAME OVER! ]===========')
print('====================================')
print(f'Eu escolhi o numero: {bot_numero}!')
print(f'Voce ganhou {contador_vitorias} vezes de mim!')