altura = input('Entre com sua altura: ')
sexo = input('Entre com o seu sexo (M/F): ')

alt = eval(altura)

if sexo == 'M':
    peso = (72.7 * alt) - 58
else:
    peso = (62.1 * alt) - 44.7
print('Seu peso ideal é:', peso)

