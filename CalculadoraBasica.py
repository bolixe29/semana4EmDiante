num1 = eval(input('Digite o primeiro número: '))
num2 = eval(input('Digite o segundo número: '))

print('Digite :  +  Somar  -  Subtrair  *  Multiplicar  /  Dividir ')

sinal = input('Escolha a operação: ')

if sinal == '+':
    print('A soma é: ', (num1 + num2))
elif sinal == '-':
    print('A subtração é: ', (num1 - num2))
elif sinal == '*':
    print('A multiplicação é: ', (num1 * num2))
elif num2 > 0:
    print('A divisão é: ', (num1 / num2))
else:
    print('Não é possível dividir')