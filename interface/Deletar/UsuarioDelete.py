import tkinter as tk
from tkinter import ttk
import requests


# Função para excluir uma avaliação pelo ID
def delete_Usuario(id_valor):
    url = f'http://localhost:5000/api/usuarios/{id_valor}'

    x = requests.delete(url)

    print(x.text)

# Criando a janela principal
def deletar_usuario():
    
    root = tk.Tk()
    root.title("Exclusão do Usuario")

    # Criando um frame para os campos de entrada
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")


    tk.Label(frame, text="ID do Usuario:").grid(row=9, column=0, sticky="w")
    delete_id_entry = ttk.Entry(frame, width=25)
    delete_id_entry.grid(row=9, column=1, padx=5, pady=5)

    # Botão para excluir avaliação
    excluir_btn = ttk.Button(frame, text="Excluir", command=lambda:delete_Usuario(delete_id_entry.get()))
    excluir_btn.grid(row=10, column=0, columnspan=2, pady=10)

    # Rodando a aplicação
    root.mainloop()
