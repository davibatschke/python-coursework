# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

valor = float(input('Digite o Valor da Compra: '))

print('\n=====[ FORMA DE PAGAMENTO ]=====')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] parcelado no cartão')
print('[ 4 ] cancelar operacao')

menu = int(input('Qual a Forma de Pagamento? '))
if menu == 1:
    valor_final = valor - (valor * (10/100))
    print(f'Valor total R$ {valor_final}')

elif menu == 2:
    valor_final = valor - (valor * (5/100))
    print(f'Valor total R$ {valor_final}')

elif menu == 3:
    vezes_cartao = int(input('Em quantas vezes sera feito? '))
    if vezes_cartao <= 2:
        valor_final = valor
        print(f'Valor total R$ {valor_final}')

    elif vezes_cartao >= 3:
        valor_final = valor + (valor * (20/100) * vezes_cartao)
        print(f'Valor total R$ {valor_final}')

elif menu == 4:
    print('Cancelando operacao...')
    exit()

else:
    print('Opcao nao Existente!')