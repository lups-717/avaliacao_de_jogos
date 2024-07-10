import tkinter as tk
from tkinter import ttk
import requests
# Função para adicionar um novo cliente à tabela
def criar_Desenvolvedora(id_valor,nome_valor,pais_valor,especialidade_valor):
    print('Atualizando desenvolvedora')
    
    # Dados a serem enviados
    data = {
        'nome': nome_valor,
        'pais_de_origem': pais_valor,
        'especialidade': especialidade_valor
    }
   

    url = f'http://localhost:5000/api/desenvolvedoras/{id_valor}'

    x = requests.put(url, json = data)

    print(x.text)

# Criando a janela principal
def atualizar_desenvolvedora():
    root = tk.Tk()
    root.title("Cadastro de Desenvolvedoras")

    # Criando um frame para os campos de entrada
    frame = ttk.Frame(root, padding="20")
    frame.grid(row=0, column=0, sticky="nsew")

    # Labels e Entradas para ID, Nome, Pais de Origem e Especialidade
    tk.Label(frame, text="ID:").grid(row=0, column=0, sticky="w", pady=5)
    id_entry = ttk.Entry(frame, width=30)
    id_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame, text="Nome:").grid(row=1, column=0, sticky="w", pady=5)
    nome_entry = ttk.Entry(frame, width=30)
    nome_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame, text="Pais de Origem:").grid(row=2, column=0, sticky="w", pady=5)
    pais_entry = ttk.Entry(frame, width=30)
    pais_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame, text="Especialidade:").grid(row=3, column=0, sticky="w", pady=5)
    especialidade_entry = ttk.Entry(frame, width=30, )
    especialidade_entry.grid(row=3, column=1, padx=5, pady=5)

    # Botão para adicionar cliente
    adicionar_btn = ttk.Button(frame, text="Adicionar Desenvolvedora", command=lambda: criar_Desenvolvedora(id_entry.get(),nome_entry.get(),pais_entry.get(),especialidade_entry.get()))
    adicionar_btn.grid(row=4, column=0, columnspan=2, pady=20)

    # Rodando a aplicação
    root.mainloop()
