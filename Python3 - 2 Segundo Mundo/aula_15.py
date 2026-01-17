# Interrompendo uma Estrutura de repetição usando o BREAK (Parte 3). As Estruturas de repetição sao usadas quando queremos facilitar uma tarefa que tem repetição.
# Porem, caso precisamos, podemos interromper um loop no Python usando o comando Break, isso pode ser usado para interrompermos um looping infinito (while True)

valor = soma = 0

# Exemplo de um uso do Break em um Loop Infinito
while True:
    valor = int(input('Digite um Valor: '))
    if valor == 6767:
        break

    soma += valor

print(f'A soma entre os valores: {soma}')