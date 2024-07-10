import tkinter as tk
from tkinter import ttk
import requests
# Função para adicionar um novo cliente à tabela

def criar_Usuario(id_valor, nome_valor, email_valor, senha_valor):
    print('Criando usuario')
    
    # Dados a serem enviados
    data = {
        'id': id_valor,
        'nome': nome_valor,
        'email': email_valor,
        'senha': senha_valor
    }
   

    url = 'http://localhost:5000/api/usuarios'

    x = requests.post(url, json = data)

    print(x.text)
    

# Criando a janela principal
def cadastro_usuario():

    root = tk.Tk()
    root.title("Cadastro do Usuário")

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

    tk.Label(frame, text="Email:").grid(row=2, column=0, sticky="w")
    email_entry = ttk.Entry(frame, width=30)
    email_entry.grid(row=2, column=1)

    tk.Label(frame, text="Senha:").grid(row=3, column=0, sticky="w")
    senha_entry = ttk.Entry(frame, width=30, show="*")
    senha_entry.grid(row=3, column=1)

    # Botão para adicionar cliente
    adicionar_btn = ttk.Button(frame, text="Adicionar Usuário", command=lambda: criar_Usuario(id_entry.get(),nome_entry.get(),email_entry.get(),senha_entry.get()))
    adicionar_btn.grid(row=4, column=0, columnspan=2, pady=10)

    # Rodando a aplicação
    root.mainloop()
