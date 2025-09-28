user = input('Digite seu usuario: ')
senha = input('Digite sua senha: ')

if user == 'admin' and str(senha) == '1234':
    print('Acesso permitido')
else:
    print('Acesso negado')