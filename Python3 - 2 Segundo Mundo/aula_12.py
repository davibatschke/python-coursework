# Condicoes Aninhadas sao estruturas condicionais dentro de outras estruturas condicionais. Para exemplificar melhor, segue o exemplo abaixo:
# Vamos montar um pequeno exemplo usando Nomes e Condicoes Aninhadas. 

nome = str(input('Digite o seu Nome: '))

# Esta eh a Condicao Aninhada, ou seja, uma Estrutura Condicional dentro de outra!
# Temos tambem a Estrutura Condicional Composta, mas nao eh esse o nosso caso agora.

# IF - Significa "Se" usado para verificar uma condicao 
if nome == 'Davi' or nome == 'Pedro':
    print('Que nome Interessante!')

# ELIF - Significa "Senao, se" tambem usado para verificar uma condicao
elif nome == 'Alice' or nome == 'Camila':
    print('Que nome Bonito!')

# ELSE - Significa  "Senao" que eh usado quando nenhuma das condicoes acima sao "validas"
else:
    print('Que nome legal!')

print(f'Tenha um bom dia, {nome}!')