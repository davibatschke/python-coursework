# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor 
# valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resposta = 'Ss'
contador = 0
valor_mais_alto = 0
valor_mais_baixo = 0
contador_media = 0

while resposta in 'Ss':
    valor = int(input('Digite um Valor: '))
    resposta = str(input('Quer continuar? [S/N] '))

    contador += 1
    contador_media += valor

    if contador == 1:
        valor_mais_alto = valor_mais_baixo = valor
    else:
        if valor > valor_mais_alto:
            valor_mais_alto = valor
        if valor < valor_mais_baixo:
            valor_mais_baixo = valor

media_final = contador_media / contador
print(f'A Média entre todos os valores é {media_final}')
print(f'O Maior valor é: {valor_mais_alto} e o Menor: {valor_mais_baixo}')