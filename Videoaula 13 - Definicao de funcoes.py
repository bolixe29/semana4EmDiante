#Uma função que calcula f(x) = x² + 1
def f(x):
    'Exemplo de documentação da função. Gerando um Docstring que será impresso com a função help()'
    res = x**2 + 1
    return res
#Uma função com dois parametros que recebe um preço e a taxa de juros e exibe o novo preço

def juros(preco, juros):
    res = preco * (1 + (juros / 100))
    return res

#O que muda no uso de return e print()
def g(x):

    res = x**2 + 1
    print(res)

    