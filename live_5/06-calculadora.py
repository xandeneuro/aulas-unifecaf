def mostrar_menu():
    print("#" * 40)
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Fatorial")
    print("6. Sair")

def calculadora():   
    mostrar_menu()
    escolha = input("Escolha uma operação (1-6): ")

    if escolha == '6':
        print("Encerrando a calculadora. Até logo!")
        return

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = num1 + num2
        print(f"Resultado: {resultado}")
    elif escolha == '2':
        resultado = num1 - num2
        print(f"Resultado: {resultado}")
    elif escolha == '3':
        resultado = num1 * num2
        print(f"Resultado: {resultado}")
    elif escolha == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    elif escolha == '5':
        if num1 >= 0 and num1.is_integer():
            resultado = 1
            for i in range(1, int(num1) + 1):
                resultado *= i
            print(f"Resultado: {resultado}")
        else:
            print("Erro: Fatorial só é definido para números inteiros não negativos.")
    else:
        print("Opção inválida. Por favor, escolha uma operação válida.")
    calculadora()

calculadora()