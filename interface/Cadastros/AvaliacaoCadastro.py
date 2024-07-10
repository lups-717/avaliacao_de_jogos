import tkinter as tk
from tkinter import ttk
import requests
# Função para adicionar uma nova avaliação à tabela
def criar_Avaliacao(id_valor,pontuacao_valor,comentario_valor,jogo_id_valor,usuario_id_valor):
    print('Criando avaliação')
    # Dados a serem enviados
    data = {
        'id': id_valor,
        'pontuacao': pontuacao_valor,
        'comentario': comentario_valor,
        'jogo_id': jogo_id_valor,
        'usuario_id': usuario_id_valor,
    }
   

    url = 'http://localhost:5000/api/avaliacoes'

    x = requests.post(url, json = data)

    print(x.text)

# Criando a janela principal
def cadastro_avaliacao():
    
    root = tk.Tk()
    root.title("Cadastro da Avaliação")

    # Criando um frame para os campos de entrada
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")

    # Labels e Entradas para ID, Pontuação, Id do Usuário, Id do Jogo e Comentários
    tk.Label(frame, text="ID:").grid(row=0, column=0, sticky="w")
    id_entry = ttk.Entry(frame, width=25)
    id_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame, text="Pontuação:").grid(row=1, column=0, sticky="w")
    pontuacao_entry = ttk.Entry(frame, width=25)
    pontuacao_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame, text="Id do Usuário:").grid(row=2, column=0, sticky="w")
    id_usuario_entry = ttk.Entry(frame, width=25)
    id_usuario_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame, text="Id do Jogo:").grid(row=3, column=0, sticky="w")
    id_jogo_entry = ttk.Entry(frame, width=25)
    id_jogo_entry.grid(row=3, column=1, padx=5, pady=5)

    # Centralizando o rótulo "Comentários"
    tk.Label(frame, text="Comentários:").grid(row=4, column=0, columnspan=2, sticky="n", pady=(10, 0))
    comentarios_entry = tk.Text(frame, width=40,height=10)
    comentarios_entry.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    # Botão para adicionar avaliação
    adicionar_btn = ttk.Button(frame, text="Adicionar Avaliação", command=lambda: criar_Avaliacao(id_entry.get(),pontuacao_entry.get(),comentarios_entry.get("1.0",tk.END),id_jogo_entry.get(),id_usuario_entry.get()))
    adicionar_btn.grid(row=6, column=0, columnspan=2, pady=10)

    # Rodando a aplicação
    root.mainloop()

