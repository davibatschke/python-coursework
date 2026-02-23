# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, 
# organizando os dados em forma tabular.

produtos = ('Intel Core i5-13400F', 1247.00, 
            'Gigabyte B760M', 1100.00,
            'Watercooler DeepCool MYSTIQUE', 647.99, 
            'Kingston Fury DDR5-5600 MHz', 1440.00,
            'Gabinete Corsair 3000D Airflow', 499.00,
            'Teclado Keychron K3', 1300.00)

print('-' * 52)
print(f'{'-' * 15} LISTAGEM DE PRODUTOS {'-' * 15}')
print('-' * 52)

for item in range(len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<38}', end='')
    else:
        print(f'R$ {produtos[item]:>10.2f}')

print('-' * 52)