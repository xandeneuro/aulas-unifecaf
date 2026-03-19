from matematica import *

import os

from colorama import Fore, Back, Style, init

init()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')    

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

    if escolha == '1':        
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = somar(num1, num2)
        limpar_tela()
        print(f"Resultado: {resultado}")       
    elif escolha == '2':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = subtrair(num1, num2)        
        limpar_tela()
        print(f"Resultado: {resultado}")
    elif escolha == '3':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = multiplicar(num1, num2)
        limpar_tela()
        print(f"Resultado: {resultado}")
    elif escolha == '4':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        if num2 != 0:
            resultado = dividir(num1, num2)
            limpar_tela()
            print(f"Resultado: {resultado}")
        else:
            limpar_tela()
            print("Erro: Divisão por zero não é permitida.")
    elif escolha == '5':
        num1 = int(input("Digite o primeiro número: "))
        if num1 >= 0 and num1.is_integer():
            limpar_tela()
            resultado = fatorial(num1)
            print(f"Resultado: {resultado}")
        else:
            limpar_tela()
            print("Erro: Fatorial só é definido para números inteiros não negativos.")
    else:
        limpar_tela()
        print(f"{Fore.RED}Opção inválida. Por favor, escolha uma operação válida.{Fore.RESET}")
    calculadora()

if __name__ == "__main__":
    calculadora()