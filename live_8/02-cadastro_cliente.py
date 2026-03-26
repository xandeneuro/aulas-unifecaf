import sqlite3
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')  

# ==============================
# CONEXÃO COM BANCO
# ==============================
def conectar():
    return sqlite3.connect("./live_8/clientes.db")


# ==============================
# CRIAR TABELA
# ==============================
def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            celular TEXT NOT NULL,
            cidade TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


# ==============================
# CREATE - CADASTRAR CLIENTE
# ==============================
def cadastrar_cliente():
    print("\n=== CADASTRAR CLIENTE ===")
    nome = input("Nome: ").strip()
    celular = input("Celular: ").strip()
    cidade = input("Cidade: ").strip()

    if nome == "" or celular == "" or cidade == "":
        print("Erro: todos os campos são obrigatórios.")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO clientes (nome, celular, cidade)
        VALUES (?, ?, ?)
    """, (nome, celular, cidade))

    conexao.commit()
    conexao.close()

    print("Cliente cadastrado com sucesso!")


# ==============================
# READ - LISTAR CLIENTES
# ==============================
def listar_clientes():
    limpar_tela()
    print("\n=== LISTA DE CLIENTES ===")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    conexao.close()

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
        return

    print("-" * 60)
    print(f"{'ID':<5}{'NOME':<20}{'CELULAR':<18}{'CIDADE':<15}")
    print("-" * 60)

    for cliente in clientes:
        id, nome, celular, cidade = cliente
        print(f"{id:<5}{nome:<20}{celular:<18}{cidade:<15}")

    print("-" * 60)


# ==============================
# READ - BUSCAR CLIENTE POR ID
# ==============================
def buscar_cliente():
    limpar_tela()
    print("\n=== BUSCAR CLIENTE ===")

    try:
        id_cliente = int(input("Digite o ID do cliente: "))
    except ValueError:
        print("Erro: ID inválido.")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id_cliente,))
    cliente = cursor.fetchone()

    conexao.close()

    if cliente:
        print("\nCliente encontrado:")
        print(f"ID: {cliente[0]}")
        print(f"Nome: {cliente[1]}")
        print(f"Celular: {cliente[2]}")
        print(f"Cidade: {cliente[3]}")
    else:
        print("Cliente não encontrado.")


# ==============================
# UPDATE - ATUALIZAR CLIENTE
# ==============================
def atualizar_cliente():
    print("\n=== ATUALIZAR CLIENTE ===")

    try:
        id_cliente = int(input("Digite o ID do cliente: "))
    except ValueError:
        print("Erro: ID inválido.")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id_cliente,))
    cliente = cursor.fetchone()

    if not cliente:
        print("Cliente não encontrado.")
        conexao.close()
        return

    print("\nDeixe em branco para manter o valor atual.")
    novo_nome = input(f"Nome [{cliente[1]}]: ").strip()
    novo_celular = input(f"Celular [{cliente[2]}]: ").strip()
    nova_cidade = input(f"Cidade [{cliente[3]}]: ").strip()

    if novo_nome == "":
        novo_nome = cliente[1]
    if novo_celular == "":
        novo_celular = cliente[2]
    if nova_cidade == "":
        nova_cidade = cliente[3]

    cursor.execute("""
        UPDATE clientes
        SET nome = ?, celular = ?, cidade = ?
        WHERE id = ?
    """, (novo_nome, novo_celular, nova_cidade, id_cliente))

    conexao.commit()
    conexao.close()

    print("Cliente atualizado com sucesso!")


# ==============================
# DELETE - EXCLUIR CLIENTE
# ==============================
def excluir_cliente():
    print("\n=== EXCLUIR CLIENTE ===")

    try:
        id_cliente = int(input("Digite o ID do cliente: "))
    except ValueError:
        print("Erro: ID inválido.")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id_cliente,))
    cliente = cursor.fetchone()

    if not cliente:
        print("Cliente não encontrado.")
        conexao.close()
        return

    confirmar = input(f"Tem certeza que deseja excluir '{cliente[1]}'? (s/n): ").lower()

    if confirmar == "s":
        cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
        conexao.commit()
        print("Cliente excluído com sucesso!")
    else:
        print("Exclusão cancelada.")

    conexao.close()


# ==============================
# MENU PRINCIPAL
# ==============================
def menu():
    criar_tabela()

    while True:
        print("\n" + "=" * 35)
        print("      SISTEMA DE CLIENTES")
        print("=" * 35)
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Buscar cliente por ID")
        print("4 - Atualizar cliente")
        print("5 - Excluir cliente")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            buscar_cliente()
        elif opcao == "4":
            atualizar_cliente()
        elif opcao == "5":
            excluir_cliente()
        elif opcao == "6":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# ==============================
# EXECUÇÃO
# ==============================
if __name__ == "__main__":
    menu()