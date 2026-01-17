# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input('Digite o Primeiro Termo: '))
razao_da_pa = int(input('Digite a Razão da PA: '))
contador = 1
total_termos = 0
mostrar_mais_termos = 10

while mostrar_mais_termos != 0:
    total_termos += mostrar_mais_termos

    while contador <= total_termos:
        print(f'{primeiro_termo} -> ', end='')
        primeiro_termo += razao_da_pa
        contador += 1
    print('PAUSA')
    mostrar_mais_termos = int(input('Quantos termos a mais deseja? '))

print('\nEncerrando a PA...')
print(f'Foram exibidos {total_termos} Termos no Total!')