# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o 
# programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 25)
valor_saque = int(input('Quanto deseja Sacar? R$'))
total = valor_saque
valor_cedula = 50
total_cedulas = 0

while True:
    if total >= valor_cedula:
        total -= valor_cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R$ {valor_cedula}')

        if valor_cedula == 50:
            valor_cedula = 20
        elif valor_cedula == 20:
            valor_cedula = 10
        elif valor_cedula == 10:
            valor_cedula = 1
        total_cedulas = 0

        if total == 0:
            break
print('=' * 25)
print('Tenha uma boa semana!')