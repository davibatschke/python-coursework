# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Digite o seu Peso: '))
altura = float(input('Digite a sua Altura (M): '))
imc = peso / (altura ** 2)

print('\nAnalisando o seu IMC...')
if imc < 18.5:
    print(f'Seu IMC: {imc:.1f} voce esta Abaixo do Peso.')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC: {imc:.1f} voce esta no Peso Ideal.')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC {imc:.1f} voce esta com Sobrepeso.')
elif imc >= 30 and imc < 40:
    print(f'Seu IMC: {imc:.1f} voce esta com Obesidade!')
else:
    print(f'Seu IMC: {imc:.1f} voce esta com Obesidade Mórbida!')