# DESAFIO 41 do Curso de Python:
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

ano_nascimento = int(input('Digite o Ano de Nascimento do Atleta: '))
idade = 2026 - ano_nascimento

if idade <= 9:
    print(f'Atleta tem {idade} anos. Categoria: MIRIM.')
elif idade > 9 and idade <= 14:
    print(f'Atleta tem {idade} anos. Categoria: INFANTIL.')
elif idade > 14 and idade <= 19:
    print(f'Atleta tem {idade} anos. Categoria: JÚNIOR')
elif idade > 19 and idade <= 25:
    print(f'Atleta tem {idade} anos. Categoria: SÊNIOR')
else:
    print(f'Atleta tem {idade} anos. Categoria: MASTER')