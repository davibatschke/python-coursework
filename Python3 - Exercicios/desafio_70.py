# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

valor_produto = total_compra = contagem_produtos = 0
valor_produto_barato = total_produtos_mais_mil = 0
nome_produto_barato = nome_produto = resposta = ''

while True:
    nome_produto = str(input('Nome do Produto: '))
    valor_produto = float(input('Qual o Preço R$'))
    contagem_produtos += 1
    total_compra += valor_produto

    if contagem_produtos == 1:
        valor_produto_barato = valor_produto
        nome_produto_barato = nome_produto
    else:
        if valor_produto < valor_produto_barato:
            nome_produto_barato = nome_produto

    if valor_produto > 1000:
        total_produtos_mais_mil += 1

    resposta = str(input('> Deseja continuar? [S/N] ')).strip()[0]
    if resposta in 'Nn':
        break

print('----- FIM DO PROGRAMA -----')
print(f'Total que foi gasto na Compra > R$ {total_compra:.2f}')
print(f'Total produtos acima de R$ 1000 > {total_produtos_mais_mil}')
print(f'Nome do produto mais barato > {nome_produto_barato}')