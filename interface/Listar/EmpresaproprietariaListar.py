import json
import tkinter as tk
from tkinter import ttk, messagebox

import requests

# Dados de exemplo para as empresas

# Função para buscar uma empresa pelo ID
def search_Empresa(table,search_id_entry,empresas):
    empresa_id = search_id_entry.get()
    for empresa in empresas:
        if str(empresa["id"]) == empresa_id:
            # Limpa a tabela antes de exibir o resultado da busca
            clear_table(table)
            # Adiciona a empresa encontrada à tabela
            table.insert("", "end", values=(
                empresa["id"], empresa["nome"], empresa["descricao"], empresa["desenvolvedora_id"]))
            return
    # Se não encontrar, limpar a tabela e mostrar mensagem
    clear_table(table)
    table.insert("", "end", values=("Não encontrado", "", "", ""))

# Função para limpar a tabela
def clear_table(table):
    for item in table.get_children():
        table.delete(item)

# Função para listar todas as empresas
def list_all_Empresas(table,empresas):
    clear_table(table)
    for empresa in empresas:
        table.insert("", "end", values=(
            empresa["id"], empresa["nome"], empresa["descricao"], empresa["desenvolvedora_id"]))

# Função para exibir a descrição completa em uma nova janela
def show_full_description(event,table,empresas):
    selected_item = table.selection()
    if selected_item:  # Verifica se um item está selecionado na tabela
        item = selected_item[0]
        values = table.item(item, "values")
        if values:  # Verifica se há valores associados ao item selecionado
            empresa_id = values[0]
            for empresa in empresas:
                if empresa["id"] == int(empresa_id):
                    full_description = empresa["Descrição"]
                    messagebox.showinfo("Descrição Completa", full_description)
                    return

# Criando a janela principal
def listar_empresa():
    data = requests.get('http://localhost:5000/api/empresas')
    empresas = json.loads(data.text)
    root = tk.Tk()
    root.title("Lista de Empresas")

    # Criando um frame para os campos de entrada
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")

    # Seção para buscar empresa por ID
    tk.Label(frame, text="Buscar Empresa por ID").grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(frame, text="ID da Empresa:").grid(row=1, column=0, sticky="w")
    search_id_entry = ttk.Entry(frame, width=25)
    search_id_entry.grid(row=1, column=1, padx=5, pady=5)

    # Botão para buscar empresa
    buscar_btn = ttk.Button(frame, text="Buscar Empresa", command=lambda:search_Empresa(table,search_id_entry,empresas))
    buscar_btn.grid(row=2, column=0, columnspan=2, pady=10)

    # Tabela para listar as empresas com evento de clique para mostrar descrição completa
    columns = ("ID", "Nome", "Descrição", "Desenvolvedora_id")
    table = ttk.Treeview(frame, columns=columns, show="headings")
    table.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    # Configurando cabeçalhos e largura das colunas
    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=150)

    # Populando a tabela com os dados de exemplo
    list_all_Empresas(table,empresas)

    # Adicionando evento de duplo clique para mostrar descrição completa
    table.bind("<Double-1>", show_full_description)

    # Separador entre as seções
    separator = ttk.Separator(frame, orient='horizontal')
    separator.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

    # Botões para listar todos e limpar busca
    listar_todos_btn = ttk.Button(frame, text="Listar Todas as Empresas", command=lambda:list_all_Empresas(table,empresas))
    listar_todos_btn.grid(row=5, column=0, padx=(10, 5), pady=10, sticky="e")

    limpar_btn = ttk.Button(frame, text="Limpar Busca", command=lambda:clear_table(table))
    limpar_btn.grid(row=5, column=1, padx=(5, 10), pady=10, sticky="w")

    # Rodando a aplicação
    root.mainloop()
