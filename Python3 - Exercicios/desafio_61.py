# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input('Digite o Primeiro Termo: '))
razao_da_pa = int(input('Digite a Razão da PA: '))
contador = 1

while contador <= 10:
    print(f'{primeiro_termo} -> ', end='')
    primeiro_termo += razao_da_pa
    contador += 1
print('Fim da PA!')