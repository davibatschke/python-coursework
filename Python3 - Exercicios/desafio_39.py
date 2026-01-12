# DESAFIO 39 do Curso de Python:
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

nascimento = int(input('Digite o seu Ano de Nascimento: '))
idade = 2026 - nascimento

print('Analisando a sua Idade...')
if idade < 18:
    print(f'Voce tem {idade} ano(s), faltam apenas {18 - idade} ano(s) para o Alistamento.')
elif idade > 18:
    print(f'Voce tem {idade} ano(s), ja se passou {idade - 18} ano(s) do seu Alistamento!')
else:
    print(f'Voce tem {idade}, voce ja deve se Alistar!')