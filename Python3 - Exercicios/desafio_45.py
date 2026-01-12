# Crie um programa que faça o computador jogar Jokenpô com você.

import random

print('===============================')
print('====[ Jokenpô com Python! ]====')
print('====[ Pedra Papel Tesoura ]====')
print('===============================')

print('-> [ 1 ] Jogar contra o Bot')
print('-> [ 2 ] Encerrar o Jokenpô')
menu_escolha = input('O que deseja fazer? ').strip()

if menu_escolha == '1':
    player = input('\nEscolha uma Jogada: ').lower().strip()
    bot = random.choice(['pedra', 'papel', 'tesoura'])
    if player == 'pedra' and bot == 'pedra' or player == 'papel' and bot == 'papel' or player == 'tesoura' and bot == 'tesoura':
        print('Parece que houve um Empate!')
        print(f'Eu tambem escolhi {bot}...')
    
    elif player == 'pedra' and bot == 'tesoura' or player == 'papel' and bot == 'pedra' or player == 'tesoura' and bot == 'papel':
        print('Poxa... Parece que voce Ganhou!')
        print(f'Eu tinha escolhido {bot}...')
    
    elif bot == 'pedra' and player == 'tesoura' or bot == 'papel' and player == 'pedra' or bot == 'tesoura' and player == 'papel':
        print('Haha! Parece que eu Ganhei!')
        print(f'Eu tinha escolhido {bot}!')

    else:
        print('Ops! Parece que sua jogada não existe!')
        print(f'No nosso Jokenpô, não temos {player.capitalize()}!')

elif menu_escolha == '2':
    print('Encerrando Jokenpô...')
    exit()

else:
    print(f'ERRO: Não encontrei a Opção que Queria.')