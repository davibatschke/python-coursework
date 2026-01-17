# Estrutura de repetição usando o BREAK (Parte 2). As Estruturas de repetição sao usadas quando queremos facilitar uma tarefa que tem repetição. Seja para mostrar
# Uma mensagem no Terminal varias vezes, mostrar uma sequencia de numeros, ou para mostrar varios itens de uma lista, ou dicionario, etc.
# No Python temos duas formas de criar uma repeticao. Aqui usamos While, que eh recomendado para quando nao sabemos o limite do que se deseja (ou quando sabemos).

mensagem = 'Oi galerinha'
contador = 0

while contador != 10:
    print(mensagem)
    contador += 1

resposta = 'Ss'

while resposta in 'Ss':
    numero = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar? [S/N]: '))

print('Fim do Programa.')