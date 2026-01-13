# Arrays são estruturas de dados que armazenam elementos em sequência na memória, por isso, conseguimos acessar um elemento pelo seu índice, que começa em 0!

# O desafio para o dia é implementar uma versão simplificada de uma lista de compras usando arrays. A lista deve permitir adicionar novos itens, remover itens 
# e listar todos os itens. Ao adicionar um novo item, o usuário deve inserir o nome do produto e a quantidade desejada. Ao remover um item, o usuário deve 
# especificar o nome do produto. Por fim, ao listar todos os itens, a lista deve exibir o nome do produto e a quantidade em um formato legível.

class ListaDeCompras:

    lista_de_itens = []
    lista_de_quantias = []

    @classmethod
    def adicionar_item(cls, item, quantidade):
        try:
            item = str(item).title().strip()
            quantia = int(quantidade)
        except ValueError:
            raise ValueError('O ITEM OU A QUANTIA ESTAO INVALIDOS')

        if not item:
            raise ValueError('ITEM PRECISA SER PREENCHIDO!')
        
        if not quantia or quantia <= 0:
            raise ValueError('QUANTIDADE PRECISA SER DEFINIDA!')
        
        cls.lista_de_itens.append(item)
        cls.lista_de_quantias.append(quantia)

        return f'Item {item} Adicionado com Sucesso!'


    @classmethod
    def remover_item(cls, item):
        if not item:
            raise ValueError('ITEM PRECISA SER PREENCHIDO!')
        
        if item not in cls.lista_de_itens:
            raise ValueError('ITEM NAO ENCONTRADO NA LISTA!')

        indice = cls.lista_de_itens.index(item)
        cls.lista_de_itens.pop(indice)
        cls.lista_de_quantias.pop(indice)

        return f'Item {item} Removido com Sucesso!'


    @classmethod
    def listar_itens_quantidades(cls):
        print(f'| {'Item'.ljust(10)} | {'Quantidade'.ljust(10)} |')

        # For Loop com Zip() do Python, para percorer duas listas ao mesmo tempo.
        for item, quantia in zip(cls.lista_de_itens, cls.lista_de_quantias):
            quantia = str(quantia)
            print(f'| {item.ljust(10)} | {quantia.ljust(10)} |')