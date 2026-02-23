# Variáveis Compostas TUPLAS. As tuplas em Python são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, 
# acessíveis por chaves individuais. Outra coisa importante elas são declaradas com parênteses, e, podemos usar o del() para deletar uma tupla.

tupla_lanches = ('Suco de Abacaxi', 'Pudim', 'Pizza', 'Strogonoff')

# Podemos fatiar uma Tupla
print(tupla_lanches[1:3])
print(tupla_lanches[-1])

# Tambem podemos usar Loops
for comida in tupla_lanches:
    print(comida)

# Podemos usar o Len()
print(len(tupla_lanches))

# Podemos juntar Tuplas
a = (67, 69, 1, 5)
b = (3, 94, 1, 4924)
c = a + b

print(c)