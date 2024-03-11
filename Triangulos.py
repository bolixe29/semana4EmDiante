a = eval(input("Entre lado 1: "))
b = eval(input("Entre lado 2: "))
c = eval(input("Entre lado 3: "))

'''maiorLado = 0

 if a > maiorLado:
    maiorLado = a
elif b > maiorLado:
    maiorLado = b
elif c > maiorLado:
    maiorLado = c '''

maiorLado = max(a, b, c)

if maiorLado < (a + b + c) - maiorLado:
    print('Os lados formam triãngulo!')
    if a == b and b == c and a == c:
        print('EQUILÁTERO')
    elif a != b and b != c and a != c:
        print('ESCALENO')
    else:
        print('ISÓSCELES')

else:
    print('Os lados NÃO formam triãngulo!')
