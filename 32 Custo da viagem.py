dis = input('Qual é a distância da viagem?')
dis = dis.upper().replace('KM','').strip()
dis = float(dis)
if dis <200:
    dis = dis * 0.50
else:
    dis = dis * 0.45
print('O valor da sua viagem foi de R$ {:.2f}.'.format(dis))