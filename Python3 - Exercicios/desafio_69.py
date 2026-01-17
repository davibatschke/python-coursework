# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

idade_pessoa = maior_idade = homens_cadastrados = mulheres_menos_20 = 0
sexo_pessoa = continuacao = ''

while True:
    print('=' * 30)
    idade_pessoa = int(input('Digite a Idade da Pessoa: '))
    sexo_pessoa = str(input('Digite o Sexo dessa Pessoa [M/F]: ')).lower().strip()
    continuacao = str(input('Deseja continuar? [S/N] '))
    
    if idade_pessoa >= 18:
        maior_idade += 1
    if sexo_pessoa in 'Mm':
        homens_cadastrados += 1
    if sexo_pessoa in 'Ff' and idade_pessoa < 20:
        mulheres_menos_20 += 1

    if continuacao not in 'Ss':
        break

print('=' * 30)
print(f'A Quantia de Pessoas Maiores de Idade: {maior_idade}')
print(f'A Quantia de Homens Cadastrados: {homens_cadastrados}')
print(f'A Quantia de Mulheres com Menos de 20 Anos: {mulheres_menos_20}')