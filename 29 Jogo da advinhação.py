from random import randint
from time import sleep
computador = randint(0,5)
print('Vou pensar em número entre 0 e 5...')
sleep(2)
print('Já sei!')
jogador = int(input('Tente adivinhar:'))
if jogador == computador:
    print('Parabéns você acertou!')
else:
    print('Você nao conseguiu hahaha. Eu pensei no número {}'.format(computador))
