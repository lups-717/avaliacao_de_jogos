import tkinter as tk
from tkinter import ttk
import requests
# Função para adicionar um novo cliente à tabela
def criar_Empresa(id_valor,nome_valor,descricao_valor,desenvolvedora_id_valor):
    print('Criando empresa')
    
    # Dados a serem enviados
    data = {
        'id': id_valor,
        'nome': nome_valor,
        'descricao': descricao_valor,
        'desenvolvedora_id': desenvolvedora_id_valor
    }
   

    url = 'http://localhost:5000/api/empresas'

    x = requests.post(url, json = data)

    print(x.text)

# Criando a janela principal
def cadastro_empresa():
    root = tk.Tk()
    root.title("Cadastro de Empresa")

    # Criando um frame para os campos de entrada
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")

    # Labels e Entradas para ID, Nome, Email e Senha
    tk.Label(frame, text="ID:").grid(row=0, column=0, sticky="w")
    id_entry = ttk.Entry(frame, width=30)
    id_entry.grid(row=0, column=1)

    tk.Label(frame, text="Nome:").grid(row=1, column=0, sticky="w")
    nome_entry = ttk.Entry(frame, width=30)
    nome_entry.grid(row=1, column=1)

    tk.Label(frame, text="Descrição:").grid(row=2, column=0, sticky="w")
    descricao_entry = ttk.Entry(frame, width=30)
    descricao_entry.grid(row=2, column=1)

    tk.Label(frame, text="Id da Desenvolvedora:").grid(row=3, column=0, sticky="w")
    desenvolvedora_id_entry = ttk.Entry(frame, width=30)
    desenvolvedora_id_entry.grid(row=3, column=1)

    # Botão para adicionar cliente
    adicionar_btn = ttk.Button(frame, text="Adicionar Empresa", command=lambda: criar_Empresa(id_entry.get(),nome_entry.get(),descricao_entry.get(),desenvolvedora_id_entry.get()))
    adicionar_btn.grid(row=4, column=0, columnspan=2, pady=10)

    # Rodando a aplicação
    root.mainloop()
