# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

comp1 = float(input('Primeiro Comprimento: '))
comp2 = float(input('Segundo Comprimento: '))
comp3 = float(input('Terceiro Comprimento: '))

if comp1 < comp2 + comp3 and comp2 < comp1 + comp3 and comp3 < comp1 + comp2:
    print('\nAnalisando o seu Triangulo...')
    if comp1 == comp2 and comp1 == comp3:
        print(f'Com os valores podemos fazer um Triangulo: EQUILÁTERO!')
    elif comp1 != comp2 and comp1 != comp3 and comp2 != comp3:
        print(f'Com os valores podemos fazer um Triangulo: ESCALENO')
    else:
        print(f'Com os valores podemos fazer um Triangulo: ISÓSCELES')
else:
    print('\nAnalisando o seu Triangulo...')
    print(f'Com os valores fornecidos nao podemos fazer um Triangulo!')