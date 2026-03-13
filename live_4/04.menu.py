opcao = None

while opcao != '0':
    print('Menu de opções:')
    print('1 - Mostrar nome')
    print('2 - Mostrar nota')
    print('3 - Mostrar situação')
    print('0 - Sair')
    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        print('Nome: João')
    elif opcao == '2':    
        print('Nota: 8.5')
    elif opcao == '3':
        print('Situação: Aprovado')
    elif opcao == '0':
        print('Saindo...')
    else:
        print('Opção inválida') 