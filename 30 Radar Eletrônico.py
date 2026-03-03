velocidade = float(input('Qual a velocidade atual do carro:'))
if velocidade > 80:
    print('Multado! Você excedeu o limite permitido que é de 80km/h.')
    multa = (velocidade - 80) * 7
    print('Sua multa foi de {:.2f}, visto que o senhor excedeu o limite em {}km/h.'.format(multa,(velocidade - 80)))
else:
    print('Tenha um bom dia, sua velocidade esta no padrão.')
