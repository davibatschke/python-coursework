#  Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('abacaxi', 'programador', 'tuplas', 'aprender', 'morango', 'python')
vogais = 'aeiou'

print('Contador de Vogais em Python!')
print('-----------------------------')

for palavra in palavras:
    print(f'\nNa palavra {palavra} temos: ', end='')

    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')

print('\n-----------------------------')