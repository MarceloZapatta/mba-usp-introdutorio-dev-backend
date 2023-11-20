# escolha um número aleatório
# entre 1 e 5
# recebe um chite
# se for igual ao número aleatório => Acertou
# senão, quase, o número secreto era {numero_secreto}

import random

input_numero_aleatorio = int(input('Escolha um número aleatório: '))
random_numero_aleatorio = random.randint(1,5)

if input_numero_aleatorio == random_numero_aleatorio:
    print('Acertou!!')
else:
    print(f'Quase! O número era: {random_numero_aleatorio}')
