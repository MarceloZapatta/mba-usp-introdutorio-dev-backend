print('IMC\n')

# peso / altura * altura

peso = int(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = round(peso  / altura ** 2)

print(f'\nO IMC é {imc}')