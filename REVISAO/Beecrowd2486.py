def tabela(alimento):
    if alimento == 'suco de laranja':
        mg = 120
    elif alimento == 'morango fresco':
        mg = 85
    elif alimento == 'mamao':
        mg = 85
    elif alimento == 'goiaba vermelha':
        mg = 70
    elif alimento == 'manga':
        mg = 56
    elif alimento == 'laranja':
        mg = 50
    elif alimento == 'brocolis':
        mg = 34
    return mg

T = 1
mg = 0
while t > 0:
    T = int(input('QUANT. ALIMENTOS: '))
    if t == 0: break

    consumo = 0

    for i in range(T):
        linha = input("Quantidade e nome alimento: ")
        n = int(linha.split(' ', 1)[0])
        alimento = linha.split(' ', 1)[1].lower()
        mg = tabela(alimento)
        consumo += n * mg

    if consumo > 130:
        print('Menos', consumo - 130,'mg')
    elif consumo < 110:
        print('Mais', 110 - consumo,'mg')
    else:
        print('Consumo Ok',consumo,'mg')
