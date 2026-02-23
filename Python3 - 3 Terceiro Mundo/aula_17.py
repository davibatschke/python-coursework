# Variáveis Compostas LISTAS. As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
# Porem diferentemente das Tuplas as listas podem sim serem modificadas atraves de metodos da propria linguagem. Alem de serem declaradas com colchetes.

lista_comidas = ['panqueca', 'frango', 'strogonoff', 'amendoim']
print(lista_comidas)

# Maneiras de adicionar um novo elemento
lista_comidas.append('batata frita')
lista_comidas.insert(0, 'tapioca')

# Maneiras de remover um elemento
# O pop remove o ultimo caso nada seja passado como parametro
lista_comidas.pop()
lista_comidas.remove('strogonoff')

# Print da lista nova com os elementos removidos e adicionados
print(lista_comidas)

# Podemos criar loops com listas
# Podemos fazer validacoes e mais uma infinidade de coisas!
for comida in lista_comidas:
    print(f'Que vontade de comer {comida}!')