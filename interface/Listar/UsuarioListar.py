import tkinter as tk
from tkinter import ttk
import json
import requests

# Função para buscar um usuário pelo ID
def search_usuario(table, search_id_entry,usuarios):
    usuario_id = search_id_entry.get()
    for usuario in usuarios:
        if str(usuario["id"]) == usuario_id:
            # Limpa a tabela antes de exibir o resultado da busca
            clear_table(table)
            # Adiciona o usuário encontrado à tabela
            table.insert("", "end", values=(
                usuario["id"], usuario["nome"], usuario["email"], usuario["senha"]))
            return
    # Se não encontrar, limpar a tabela e mostrar mensagem
    clear_table(table)
    table.insert("", "end", values=("Não encontrado", "", "", ""))

# Função para limpar a tabela
def clear_table(table):
    for item in table.get_children():
        table.delete(item)

# Função para listar todos os usuários
def list_all_usuarios(table,usuarios):
    clear_table(table)
    for usuario in usuarios:
        table.insert("", "end", values=(
            usuario["id"], usuario["nome"], usuario["email"], usuario["senha"]))

# Criando a janela principal

def listar_usuario():
    data = requests.get('http://localhost:5000/api/usuarios')
    usuarios = json.loads(data.text)
    root = tk.Tk()
    root.title("Lista de Usuários")

    # Criando um frame para os campos de entrada
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")

    # Seção para buscar usuário por ID
    tk.Label(frame, text="Buscar Usuário por ID").grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(frame, text="ID do Usuário:").grid(row=1, column=0, sticky="w")
    search_id_entry = ttk.Entry(frame, width=25)
    search_id_entry.grid(row=1, column=1, padx=5, pady=5)

    # Botão para buscar usuário
    buscar_btn = ttk.Button(frame, text="Buscar Usuário", command=lambda: search_usuario(table,search_id_entry,usuarios))
    buscar_btn.grid(row=2, column=0, columnspan=2, pady=10)

    # Tabela para listar os usuários
    columns = ("ID", "Nome", "Email", "Senha")
    table = ttk.Treeview(frame, columns=columns, show="headings")
    table.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    # Configurando cabeçalhos e largura das colunas
    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=150)

    # Populando a tabela com os dados de exemplo
    list_all_usuarios(table,usuarios)

    # Separador entre as seções
    separator = ttk.Separator(frame, orient='horizontal')
    separator.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

    # Botões para listar todos e limpar busca
    listar_todos_btn = ttk.Button(frame, text="Listar Todos os Usuários", command=lambda: list_all_usuarios(table,usuarios))
    listar_todos_btn.grid(row=5, column=0, padx=(10, 5), pady=10, sticky="e")

    limpar_btn = ttk.Button(frame, text="Limpar Busca", command=lambda: clear_table(table))
    limpar_btn.grid(row=5, column=1, padx=(5, 10), pady=10, sticky="w")

    # Rodando a aplicação
    root.mainloop()