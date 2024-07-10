import tkinter as tk
from tkinter import ttk
import requests
# Função para adicionar um novo cliente à tabela
def criar_Jogo(id_valor, titulo_valor,descricao_valor,genero_valor,data_valor,empresa_id_valor):
    print('Atualizando jogo')
    
    # Dados a serem enviados
    data = {
        'titulo': titulo_valor,
        'descricao': descricao_valor,
        'genero': genero_valor,
        'data_de_lancamento': data_valor,
        'empresa_proprietaria_id': empresa_id_valor
    }
   

    url = f'http://localhost:5000/api/jogos/{id_valor}'

    x = requests.put(url, json = data)

    print(x.text)

# Criando a janela principal
def atualizar_jogo():
    root = tk.Tk()
    root.title("Cadastro de Jogo")

    # Criando um frame para os campos de entrada
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")

    # Labels e Entradas para ID, Nome, Email e Senha
    tk.Label(frame, text="ID:").grid(row=0, column=0, sticky="w")
    id_entry = ttk.Entry(frame, width=30)
    id_entry.grid(row=0, column=1)

    tk.Label(frame, text="Título:").grid(row=1, column=0, sticky="w")
    titulo_entry = ttk.Entry(frame, width=30)
    titulo_entry.grid(row=1, column=1)

    tk.Label(frame, text="Descrição:").grid(row=2, column=0, sticky="w")
    descricao_entry = ttk.Entry(frame, width=30)
    descricao_entry.grid(row=2, column=1)

    tk.Label(frame, text="Gênero:").grid(row=3, column=0, sticky="w")
    genero_entry = ttk.Entry(frame, width=30)
    genero_entry.grid(row=3, column=1)

    tk.Label(frame, text="Data de lançamento:").grid(row=4, column=0, sticky="w")
    data_entry = ttk.Entry(frame, width=30)
    data_entry.grid(row=4, column=1)

    tk.Label(frame, text="Id da Empresa").grid(row=5, column=0, sticky="w")
    empresa_id_entry = ttk.Entry(frame, width=30)
    empresa_id_entry.grid(row=5, column=1)

    # Botão para adicionar cliente
    adicionar_btn = ttk.Button(frame, text="Atualizar Jogo", command=lambda: criar_Jogo(id_entry.get(),titulo_entry.get(),descricao_entry.get(),genero_entry.get(),data_entry.get(),empresa_id_entry.get()))
    adicionar_btn.grid(row=6, column=0, columnspan=2, pady=10)

    # Rodando a aplicação
    root.mainloop()
