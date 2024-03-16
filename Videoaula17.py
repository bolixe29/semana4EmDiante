#Exemplo dado em aula de estrutura de repetição que soma números pares de 1 a 100
acum = 0
for x in range(1, 100):
    if x % 2 == 0:
        acum = acum + x
print(acum)