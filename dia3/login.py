login = ''
senha = ''
print ('ok')
login = input ('login: ').lower().strip()
senha = input ('senha: ').strip()

if login == 'arthur' and senha == '1234':
    print ('seja bem vindo')
else:
    print ('acesso negado')