print('**'*20)
user = input('Usuário: ')
password = input('Senha: ')
print('=='*20)
while user == password:
  print('A senha não pode ser igual ao usuário!!! - Error 500')
  password= input('Informe uma senha diferente: ')

print(f'Cadastro efetuado com sucesso\n - Seja Bem Vindo {user}')