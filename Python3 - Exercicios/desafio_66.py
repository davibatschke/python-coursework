# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

valor = soma = contador = 0

while True:
    valor = int(input('Digite um Valor: '))
    if valor == 999:
        break

    soma += valor
    contador += 1

print(f'\nQuantidade de números foram digitados: {contador}')
print(f'A soma entre todos os valores foi de: {soma}')