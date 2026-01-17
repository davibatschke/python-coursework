# Estrutura de repetição usando o FOR (Parte 1). As Estruturas de repetição sao usadas quando queremos facilitar uma tarefa que tem repetição. Seja para mostrar
# Uma mensagem no Terminal varias vezes, mostrar uma sequencia de numeros, ou para mostrar varios itens de uma lista, ou dicionario, etc.
# Porem no Python temos duas formas de criar uma repeticao, aqui usamos o For, que eh recomendado quando sabemos o limite de onde queremos chegar!

for i in range(10):
    print('Oi')

print('')
n1 = int(input('Comeco: '))
n2 = int(input('Final: '))
n3 = int(input('Ordem: '))

for i in range(n1, n2 + 1, n3):
    print(i)