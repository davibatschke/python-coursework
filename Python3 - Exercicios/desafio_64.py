# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

valor = int(input('Digite um Valor (999 Pra Parar): '))
soma_total = contagem_total = 0

while valor != 999:
    soma_total += valor
    contagem_total += 1

    valor = int(input('Digite mais um Valor: '))

print(f'A soma entre todos os Valores: {soma_total}')
print(f'O total de Valores digitados foi de: {contagem_total}')