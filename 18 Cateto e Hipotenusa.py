from math import hypot
c1 = float(input( 'Comprimento do cateto oposto:'))
c2 = float(input( 'Comprimento do cateto adjacente:'))
h = hypot(c1,c2)
print('A hipotenusa de {} e {} é {:.2f}'.format(c1,c2,h))
