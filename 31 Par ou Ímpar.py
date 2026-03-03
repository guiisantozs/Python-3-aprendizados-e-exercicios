num = int(input('Digite um número:'))
resultado = num % 2
if resultado == 0:
    print('O número {} é Par'.format(num))
else:
    print('{} é um numero impar'.format(num))