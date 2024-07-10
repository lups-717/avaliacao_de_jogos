import tkinter as tk
from tkinter import ttk
import requests
import json
# Dados de exemplo para os desenvolvedores

# Função para buscar um desenvolvedor pelo ID
def search_Desenvolvedor(table,search_id_entry,desenvolvedoras):
    desenvolvedor_id = search_id_entry.get()
    for desenvolvedor in desenvolvedoras:
        if str(desenvolvedor["id"]) == desenvolvedor_id:
            # Limpa a tabela antes de exibir o resultado da busca
            clear_table(table)
            # Adiciona o desenvolvedor encontrado à tabela
            table.insert("", "end", values=(
                desenvolvedor["id"], desenvolvedor["nome"], desenvolvedor["pais_de_origem"],
                desenvolvedor["especialidade"]))
            return
    # Se não encontrar, limpar a tabela e mostrar mensagem
    clear_table(table)
    table.insert("", "end", values=("Não encontrado", "", "", ""))

# Função para limpar a tabela
def clear_table(table):
    for item in table.get_children():
        table.delete(item)

# Função para listar todos os desenvolvedores
def list_all_Desenvolvedores(table,desenvolvedoras):
    clear_table(table)
    for desenvolvedor in desenvolvedoras:
        table.insert("", "end", values=(
            desenvolvedor["id"], desenvolvedor["nome"], desenvolvedor["pais_de_origem"],
            desenvolvedor["especialidade"]))

# Criando a janela principal
def listar_desenvolvedora():
    data = requests.get('http://localhost:5000/api/desenvolvedoras')
    desenvolvedoras = json.loads(data.text)
    root = tk.Tk()
    root.title("Lista de Desenvolvedores")

    # Criando um frame para os campos de entrada
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")

    # Seção para buscar desenvolvedor por ID
    tk.Label(frame, text="Buscar Desenvolvedor por ID").grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(frame, text="ID do Desenvolvedor:").grid(row=1, column=0, sticky="w")
    search_id_entry = ttk.Entry(frame, width=25)
    search_id_entry.grid(row=1, column=1, padx=5, pady=5)

    # Botão para buscar desenvolvedor
    buscar_btn = ttk.Button(frame, text="Buscar Desenvolvedor", command=lambda:search_Desenvolvedor(table,search_id_entry,desenvolvedoras))
    buscar_btn.grid(row=2, column=0, columnspan=2, pady=10)

    # Tabela para listar os desenvolvedores
    columns = ("ID", "Nome", "Pais de Origem", "Especialidade")
    table = ttk.Treeview(frame, columns=columns, show="headings")
    table.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    # Configurando cabeçalhos e largura das colunas
    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=150)

    # Populando a tabela com os dados de exemplo
    list_all_Desenvolvedores(table,desenvolvedoras)

    # Separador entre as seções
    separator = ttk.Separator(frame, orient='horizontal')
    separator.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

    # Botões para listar todos e limpar busca
    listar_todos_btn = ttk.Button(frame, text="Listar Todos os Desenvolvedores", command=lambda:list_all_Desenvolvedores(table,desenvolvedoras))
    listar_todos_btn.grid(row=5, column=0, padx=(10, 5), pady=10, sticky="e")

    limpar_btn = ttk.Button(frame, text="Limpar Busca", command=lambda:clear_table(table))
    limpar_btn.grid(row=5, column=1, padx=(5, 10), pady=10, sticky="w")

    # Rodando a aplicação
    root.mainloop()
