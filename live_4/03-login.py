senha_cadastrada = '123456'
senha_digitada = input('Digite a senha: ')

while senha_digitada != senha_cadastrada:
    print('Senha incorreta, tente novamente!')
    senha_digitada = input('Digite a senha: ')

print('Acesso permitido!')