
import os

from colorama import Fore, Back, Style, init

init()

banco_dados = ['tarefa 1', 'tarefa 2', 'tarefa 3']

def exibir_menu():
    print('#'*20)
    print("1. Cadastrar tarefa")
    print("2. Listar as tarefas")
    print("3. Modificar tarefa")
    print("4. Remover tarefa")
    print("0. Sair")
    print('#'*20)   

def cadastrar_tarefa():
   tarefa_nova = input("Digite uma nova tarefa: ")
   banco_dados.append(tarefa_nova)
   print("Tarefa cadastrada com sucesso!")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')    

def listar_tarefas():
    limpar_tela()
    for pos, tarefa in enumerate(banco_dados):
        print(f'{pos + 1}-{tarefa}')

def modificar_tarefa():
    listar_tarefas()  
    pos = int(input("Escolha o numero da tarefa que deseja modificar: "))
    banco_dados[pos - 1] = input("Digite a nova tarefa: ")


def remover_tarefa():
   listar_tarefas()  
   pos = int(input("Escolha o numero da tarefa que deseja remover: "))
   #del banco_dados[pos - 1]
   banco_dados.pop(pos - 1)

def lista_tarefas():
    tarefas = []
    while True:
        exibir_menu()
        resposta = int(input("Escolha uma opção: ")) 

        if resposta == 1:
            cadastrar_tarefa()
        elif resposta == 2:
            listar_tarefas()
        elif resposta == 3:
            modificar_tarefa()
        elif resposta == 4:
            remover_tarefa()
        elif resposta == 0:
            print("Saindo do sistema...")
            break
        else:
            print(f"{Fore.RED}Opção inválida{Style.RESET_ALL}")

    

if __name__ == "__main__":
    lista_tarefas()