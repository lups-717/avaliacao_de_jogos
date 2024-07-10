import json
import tkinter as tk
from tkinter import ttk, messagebox

import requests

# Dados de exemplo para as avaliações

# Função para buscar uma avaliação pelo ID
def search_Avaliacao(table,search_id_entry,avaliacoes):
    avaliacao_id = search_id_entry.get()
    for avaliacao in avaliacoes:
        if str(avaliacao["id"]) == avaliacao_id:
            # Limpa a tabela antes de exibir o resultado da busca
            clear_table(table)
            # Adiciona a avaliação encontrada à tabela
            table.insert("", "end", values=(
                avaliacao["id"], avaliacao["pontuacao"], avaliacao["usuario_id"],
                avaliacao["jogo_id"], avaliacao["comentario"]))
            return
    # Se não encontrar, limpar a tabela e mostrar mensagem
    clear_table(table)
    table.insert("", "end", values=("Não encontrado", "", "", "", ""))

# Função para limpar a tabela
def clear_table(table):
    for item in table.get_children():
        table.delete(item)

# Função para listar todas as avaliações
def list_all_Avaliacoes(table,avaliacoes):
    clear_table(table)
    for avaliacao in avaliacoes:
        table.insert("", "end", values=(
            avaliacao["id"], avaliacao["pontuacao"], avaliacao["usuario_id"],
            avaliacao["jogo_id"], avaliacao["comentario"]))

# Função para exibir o comentário completo em uma nova janela
def show_full_comment(table,avaliacoes):
    selected_item = table.selection()
    if selected_item:  # Verifica se um item está selecionado na tabela
        item = selected_item[0]
        values = table.item(item, "values")
        if values:  # Verifica se há valores associados ao item selecionado
            avaliacao_id = values[0]
            for avaliacao in avaliacoes:
                if avaliacao["ID"] == int(avaliacao_id):
                    full_comment = avaliacao["Comentários"]
                    messagebox.showinfo("Comentário Completo", full_comment)
                    return

# Criando a janela principal
def listar_avaliacao():
    data = requests.get('http://localhost:5000/api/avaliacoes')
    avaliacoes = json.loads(data.text)
    root = tk.Tk()
    root.title("Lista de Avaliações")

    # Criando um frame para os campos de entrada
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")

    # Seção para buscar avaliação por ID
    tk.Label(frame, text="Buscar Avaliação por ID").grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(frame, text="ID da Avaliação:").grid(row=1, column=0, sticky="w")
    search_id_entry = ttk.Entry(frame, width=25)
    search_id_entry.grid(row=1, column=1, padx=5, pady=5)

    # Botão para buscar avaliação
    buscar_btn = ttk.Button(frame, text="Buscar Avaliação", command=lambda:search_Avaliacao(table,search_id_entry,avaliacoes))
    buscar_btn.grid(row=2, column=0, columnspan=2, pady=10)

    # Tabela para listar as avaliações com evento de clique para mostrar comentário completo
    columns = ("ID", "Pontuação", "Id do Usuário", "Id do Jogo", "Comentários")
    table = ttk.Treeview(frame, columns=columns, show="headings")
    table.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    # Configurando cabeçalhos e largura das colunas
    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=100 if col != "Comentários" else 300)

    # Populando a tabela com os dados de exemplo
    list_all_Avaliacoes(table,avaliacoes)

    # Adicionando evento de duplo clique para mostrar comentário completo
    table.bind("<Double-1>", lambda:show_full_comment(table,avaliacoes))

    # Separador entre as seções
    separator = ttk.Separator(frame, orient='horizontal')
    separator.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

    # Botões para listar todos e limpar busca
    listar_todos_btn = ttk.Button(frame, text="Listar Todas Avaliações", command=lambda:list_all_Avaliacoes(table,avaliacoes))
    listar_todos_btn.grid(row=5, column=0, padx=(10, 5), pady=10, sticky="e")

    limpar_btn = ttk.Button(frame, text="Limpar Busca", command=lambda:clear_table(table))
    limpar_btn.grid(row=5, column=1, padx=(5, 10), pady=10, sticky="w")

    # Rodando a aplicação
    root.mainloop()
