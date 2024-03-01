#Mostrou uso da função print() e uso de separador e pular linhas

dia = 29
mes = 0o02
ano = 2024

print(dia, mes, ano, sep='/')
print(dia, mes, ano, sep='/', end='.\n')

#Uso básico da função input()

nome = input("Escreva um nome: ")
digito = input("Escreva um número: ")
print(nome)
print(type(digito))

#Na sequência abordou a função eval() usando o exemplo de Conversão de °C em °F
c = input('Temperatura em °C: ')
c_temp = eval(c)
f = 1.8 * c_temp + 32

print(f, '°F')





