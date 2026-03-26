
import os
import sqlite3

from colorama import Fore, Back, Style, init
init()

conexao = sqlite3.connect('./live_8/tarefas.db')
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tarefa TEXT NOT NULL,
        feito INTEGER NOT NULL DEFAULT 0
    )
""")

conexao.commit()

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
    print('id escolhido', id_escolhido)

def cadastrar_tarefa():
    tarefa_nova = input("Digite uma nova tarefa: ")
    cursor.execute("INSERT INTO tarefas (tarefa) VALUES (?)", (tarefa_nova,))
    conexao.commit()   


def listar_tarefas():
    limpar_tela()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    print(f"{'ID':<5} {'TAREFA':<30} {'STATUS'}")
    print('-'*50)
    for item in tarefas:
        id, tarefa, feito = item
        if feito:
            status = Fore.GREEN + 'Feito' + Style.RESET_ALL
        else:
            status = Fore.RED + 'Pendente' + Style.RESET_ALL  
        print(f"{id:<5} {tarefa:<30} {status}")
    print('-'*50)

def modificar_tarefa():
    listar_tarefas()
    id_escolhido = int(input("Escolha o ID da tarefa que deseja modificar: "))
    tarefa_nova = input("Digite a nova tarefa: ")
    cursor.execute("UPDATE tarefas SET tarefa = ? WHERE id = ?", (tarefa_nova, id_escolhido))
    conexao.commit()

def remover_tarefa():
    listar_tarefas()
    id_escolhido = int(input("Escolha o ID da tarefa que deseja remover: "))
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_escolhido,))
    conexao.commit()

def trocar_status():
    listar_tarefas()
    id_escolhido = int(input("Escolha o ID da tarefa que deseja alterar o status: "))
    cursor.execute("UPDATE tarefas SET feito = NOT feito WHERE id = ?", (id_escolhido,))
    conexao.commit()


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