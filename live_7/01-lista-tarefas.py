
import os

from colorama import Fore, Back, Style, init

init()

banco_dados = [
    {"id": 1, "tarefa": "Comprar passagem","feito":False},
    {"id": 2, "tarefa": "Pagar aluguel","feito":True},
    {"id": 3, "tarefa": "Correr no parque","feito":False},
]

proximo_id = 4

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')    



def exibir_menu():
    print('#'*20)
    print("1. Cadastrar tarefa")
    print("2. Listar as tarefas")
    print("3. Modificar tarefa")
    print("4. Remover tarefa")
    print("5. Trocar status")
    print("0. Sair")
    print('#'*20)  

def buscar_tarefa_por_id(id_escolhido):
    for item in banco_dados:
        if item['id'] == id_escolhido:
            return item
    return None

def cadastrar_tarefa():
   limpar_tela()
   listar_tarefas() 
   global proximo_id
   tarefa_nova = input("Digite uma nova tarefa: ")
   banco_dados.append({"id": proximo_id, "tarefa": tarefa_nova,"feito":False})
   proximo_id += 1


def listar_tarefas():
    limpar_tela()
    print(f"{'ID':<5} {'TAREFA':<30} {'STATUS'}")
    print('-'*50)
    for item in banco_dados:
        if item['feito']:
            status = Fore.GREEN + 'Feito' + Style.RESET_ALL
        else:
            status = Fore.RED + 'Pendente' + Style.RESET_ALL  
        print(f"{item['id']:<5} {item['tarefa']:<30} {status}")
    print('-'*50)

def modificar_tarefa():
    listar_tarefas()  
    id_escolhido = int(input("Escolha o ID da tarefa que deseja modificar: "))
    tarefa = buscar_tarefa_por_id(id_escolhido)
    if tarefa is None:
        print("Tarefa nao encontrada")
        return
    tarefa['tarefa'] = input(f"Digite a nova tarefa (atual: {tarefa['tarefa']} ): ")
    print("Tarefa modificada com sucesso!")

def remover_tarefa():
    listar_tarefas()  
    id_escolhido = int(input("Escolha o ID da tarefa que deseja remover: "))
    tarefa = buscar_tarefa_por_id(id_escolhido)
    if tarefa is None:
        print("Tarefa nao encontrada")
        return
    banco_dados.remove(tarefa)
    print("Tarefa removida com sucesso!")

def trocar_status():
    listar_tarefas()  
    id_escolhido = int(input("Escolha o ID da tarefa que deseja alterar o status: "))
    tarefa = buscar_tarefa_por_id(id_escolhido)
    if tarefa is None:
        print(f"{Fore.RED}Tarefa nao encontrada{Style.RESET_ALL}")
        return
    tarefa['feito'] = not tarefa['feito']
    print("Status da tarefa alterado com sucesso!")


def app():
    while True:
        exibir_menu()
        resposta = int(input("Escolha uma opção: ")) 

        if resposta == 1:
            cadastrar_tarefa()
            #print("Cadastrando tarefas")
        elif resposta == 2:
            listar_tarefas()
            #print("Listando tarefas")
        elif resposta == 3:
           modificar_tarefa()
           #print("Modificando tarefas")
        elif resposta == 4:
           remover_tarefa()
           #print("Removendo tarefas")
        elif resposta == 5:
           trocar_status()
           #print("Marcando tarefas como feitas")
        elif resposta == 0:
            print("Saindo do sistema...")
            break
        else:
            print(f"{Fore.RED}Opção inválida{Style.RESET_ALL}")

    

if __name__ == "__main__":
    app()