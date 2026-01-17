# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

import random

print('Acabei de pensar em valor. Consegue adivinhar?')

numero_escolhido = random.randint(0, 10)
escolha_jogador = int(input('Escolha um Valor entre 0 a 10. '))
contador_tentativas = 0

while escolha_jogador != numero_escolhido:
    if escolha_jogador > numero_escolhido:
        print(f'Menos... Tente novamente.')
        escolha_jogador = int(input('Escolha outro valor: '))
        contador_tentativas += 1
    if escolha_jogador < numero_escolhido:
        print(f'Mais... Tente novamente.')
        escolha_jogador = int(input('Escolha outro valor: '))
        contador_tentativas += 1

print(f'Parabens! Voce conseguiu em apenas {contador_tentativas} Tentativas!')