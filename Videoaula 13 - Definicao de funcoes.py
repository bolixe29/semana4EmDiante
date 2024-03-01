#Uma função que calula f(x) = x² + 1

def f(x):
    res = x**2 + 1
    return res

#Uma função com vários parametros

def juros(preco, juros):
    res = preco * (1 + (juros / 100))
    return res

#O que muda no uso de return e print()

def g(x):
    res = x**2 + 1
    print(res)