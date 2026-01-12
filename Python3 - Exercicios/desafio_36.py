# DESAFIO 36 do Curso de Python:
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai 
# pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Digite o Valor da Casa: R$ '))
salario = float(input('Digite o seu Salario: R$ '))
financiamento = int(input('Quantos Anos de Financiamento: '))

prestacao = valor_casa / (financiamento * 12)
minimo_salario = salario * 30 / 100

print(f'Com uma Casa de R$ {valor_casa:.2f} em {financiamento * 12}x por R$ {prestacao:.2f}')
if prestacao <= minimo_salario:
    print(f'O seu Emprestimo foi CONCEDIDO!')
else:
    print(f'O seu Emprestimo foi NEGADO!')
