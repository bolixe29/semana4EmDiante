logins_validos = ['joe', 'sue', ' hani', 'sophie']

usuario = input('Entre com seu usuário: ')

if usuario in logins_validos:
    print('ACCESS GRANTED!')
else:
    print('LOGIN FAILED')


print("FIM.")



