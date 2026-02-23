d = float(input('Quantos dias foram alugados:'))
km = float(input('Quantos km foram rodados:'))
pf = d * 60 + km * 0.15
print('O total a pagar é de R${:.2F}.'.format(pf))
