import json
import tkinter as tk
from tkinter import ttk, messagebox
import requests
# Dados de exemplo para os jogos
# jogos = [
#     {"ID": 1, "Título": "Jogo A", "Descrição": "Descrição do Jogo A", "Gênero": "Ação", "Data de Lançamento": "2023-01-15", "Empresa_Proprietária_id": 101},
#     {"ID": 2, "Título": "Jogo B", "Descrição": "Descrição do Jogo B", "Gênero": "Aventura", "Data de Lançamento": "2022-07-20", "Empresa_Proprietária_id": 102},
#     {"ID": 3, "Título": "Jogo C", "Descrição": "Descrição do Jogo C", "Gênero": "RPG", "Data de Lançamento": "2023-05-08", "Empresa_Proprietária_id": 103},
#     # Adicione mais jogos conforme necessário
# ]

# Função para buscar um jogo pelo ID
def search_Jogo(table,search_id_entry,jogos):
    jogo_id = search_id_entry.get()
    for jogo in jogos:
        if str(jogo["id"]) == jogo_id:
            # Limpa a tabela antes de exibir o resultado da busca
            clear_table(table)
            # Adiciona o jogo encontrado à tabela
            table.insert("", "end", values=(
                jogo["id"], jogo["titulo"], jogo["descricao"], jogo["genero"], jogo["data_de_lancamento"], jogo["empresa_proprietaria_id"]))
            return
    # Se não encontrar, limpar a tabela e mostrar mensagem
    clear_table(table)
    table.insert("", "end", values=("Não encontrado", "", "", "", "", ""))

# Função para limpar a tabela
def clear_table(table):
    for item in table.get_children():
        table.delete(item)

# Função para listar todos os jogos
def list_all_Jogos(table,jogos):
    clear_table(table)
    for jogo in jogos:
        table.insert("", "end", values=(
             jogo["id"], jogo["titulo"], jogo["descricao"], jogo["genero"], jogo["data_de_lancamento"], jogo["empresa_proprietaria_id"]))

# Função para exibir a descrição completa em uma nova janela
def show_full_description(event,table,jogos):
    selected_item = table.selection()
    if selected_item:  # Verifica se um item está selecionado na tabela
        item = selected_item[0]
        values = table.item(item, "values")
        if values:  # Verifica se há valores associados ao item selecionado
            jogo_id = values[0]
            for jogo in jogos:
                if jogo["id"] == int(jogo_id):
                    full_description = jogo["descricao"]
                    messagebox.showinfo("Descrição Completa", full_description)
                    return

# Criando a janela principal
def listar_jogo():
    data = requests.get('http://localhost:5000/api/jogos')
    jogos = json.loads(data.text)
    root = tk.Tk()
    root.title("Lista de Jogos")

    # Criando um frame para os campos de entrada
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")

    # Seção para buscar jogo por ID
    tk.Label(frame, text="Buscar Jogo por ID").grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(frame, text="ID do Jogo:").grid(row=1, column=0, sticky="w")
    search_id_entry = ttk.Entry(frame, width=25)
    search_id_entry.grid(row=1, column=1, padx=5, pady=5)

    # Botão para buscar jogo
    buscar_btn = ttk.Button(frame, text="Buscar Jogo", command=lambda:search_Jogo(table,search_id_entry,jogos))
    buscar_btn.grid(row=2, column=0, columnspan=2, pady=10)

    # Tabela para listar os jogos com evento de clique para mostrar descrição completa
    columns = ("ID", "Título", "Descrição", "Gênero", "Data de Lançamento", "Empresa Proprietária ID")
    table = ttk.Treeview(frame, columns=columns, show="headings")
    table.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    # Configurando cabeçalhos e largura das colunas
    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=150)

    # Populando a tabela com os dados de exemplo
    list_all_Jogos(table,jogos)

    # Adicionando evento de duplo clique para mostrar descrição completa
    table.bind("<Double-1>", lambda:show_full_description(table,jogos))

    # Separador entre as seções
    separator = ttk.Separator(frame, orient='horizontal')
    separator.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

    # Botões para listar todos e limpar busca
    listar_todos_btn = ttk.Button(frame, text="Listar Todos os Jogos", command=lambda: list_all_Jogos(table,jogos))
    listar_todos_btn.grid(row=5, column=0, padx=(10, 5), pady=10, sticky="e")

    limpar_btn = ttk.Button(frame, text="Limpar Busca", command=lambda:clear_table(table))
    limpar_btn.grid(row=5, column=1, padx=(5, 10), pady=10, sticky="w")

    # Rodando a aplicação
    root.mainloop()
