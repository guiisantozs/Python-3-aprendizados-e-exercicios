from math import sin, cos, tan, radians
an = float(input( 'Digite o valor do angulo:'))
s = sin(radians(an))
c = cos(radians(an))
t = tan(radians(an))
print('O angulo de {} tem o seno de {:.2f}.'.format(an,s))
print('O angulo de {} tem o cosseno de {:.2f}.'.format(an,c))
print('O angulo de {} tem a tangente de {:.2f}'.format(an,t))