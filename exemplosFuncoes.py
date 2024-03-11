import math

def negativos(lista):

    for i in lista:
        if i < 0:
            print(i)
def perimetro(raio):

    if raio <= 0:
        print('Raio deve ser positivo')

    return 2 * math.pi * raio

def media2NotasPesos(n1, n2):

    media = 0.4 * n1 + 0.6 * n2

    return media
def meuimc(peso, altura):

    indice = peso / (altura**2)

    if  indice < 18.5:
        print('Frango', indice)
    elif 18.5 <= indice <25:
        print('Normal', indice)
    elif indice >= 25:
        print('Baleeeia', indice)