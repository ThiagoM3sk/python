from random import randint
from time import sleep # importa a função "dormir" que faz com que o computador espere em segundos  para exibir
user = int(input('Digite um número de 0 a 5: '))
computador = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
if user == computador:
    print('Parabéns, você acertou! O número era {}'.format(computador))
else:
    print('Que pena, você errou! O número era {}'.format(computador))
print('Obrigado por partcipar!')
print('--FIM--')
