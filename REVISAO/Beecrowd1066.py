pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(0,5):
    x = int(input("ENTRE NÚMERO: "))
    if x%2 == 0:
        pares += 1
    else:
        impares += 1
    if x > 0:
        positivos +=1
    elif x < 0:
        negativos += 1

print(pares, "valor(es) par(es)")
print(impares, "valor(es) ímpar(es)")
print(positivos, "valor(es) positivo(s)")
print(negativos, "valor(es) negativo(s)")