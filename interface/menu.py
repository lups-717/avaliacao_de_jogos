import tkinter as tk
from tkinter import ttk
from Cadastros import UsuarioCadastro, JogoCadastro, DesenvolvedoraCadastro, EmpresaproprietariaCadastro, AvaliacaoCadastro
from Listar import UsuarioListar, JogoListar, EmpresaproprietariaListar, DesenvolvedoraListar, AvaliacaoListar
from Atualizar import UsuarioCadastroAtualizar,AvaliacaoAtualizar,DesenvolvedoraAtualizar,EmpresaproprietariaAtualizar, JogoAtualizar
from Deletar import UsuarioDelete, AvaliacaoDelete,JogoDelete,EmpresaproprietariaDelete,DesenvolvedoraDelete
# Funções para cada opção do menu
def abrir_pagina_cadastro_Usuario():
    print("Abrindo página de cadastro de Usuário")
    UsuarioCadastro.cadastro_usuario()
    
def abrir_pagina_cadastro_Empresa():
    print("Abrindo página de cadastro de Empresa")
    EmpresaproprietariaCadastro.cadastro_empresa()
def abrir_pagina_cadastro_Avaliacao():
    print("Abrindo página de cadastro de Avaliação")
    AvaliacaoCadastro.cadastro_avaliacao()

def abrir_pagina_cadastro_Jogo():
    print("Abrindo página de cadastro de Jogo")
    JogoCadastro.cadastro_jogo()
def abrir_pagina_cadastro_Desenvolvedora():
    print("Abrindo página de cadastro de Desenvolvedora")
    DesenvolvedoraCadastro.cadastro_desenvolvedora()


def abrir_pagina_listagem_Usuario():
    print("Abrindo página de listagem de Usuários")
    UsuarioListar.listar_usuario()

def abrir_pagina_listagem_Empresa():
    print("Abrindo página de listagem de Empresas")
    EmpresaproprietariaListar.listar_empresa()
def abrir_pagina_listagem_Avaliacao():
    print("Abrindo página de listagem de Avaliações")
    AvaliacaoListar.listar_avaliacao();
def abrir_pagina_listagem_Jogo():
    print("Abrindo página de listagem de Jogos")
    JogoListar.listar_jogo()
def abrir_pagina_listagem_Desenvolvedora():
    print("Abrindo página de listagem de Desenvolvedoras")
    DesenvolvedoraListar.listar_desenvolvedora()


def abrir_pagina_atualizacao_Usuario():
    print("Abrindo página de atualização de Usuário")
    UsuarioCadastroAtualizar.atualizar_usuario()
def abrir_pagina_atualizacao_Empresa():
    print("Abrindo página de atualização de Empresa")
    EmpresaproprietariaAtualizar.atualizar_empresa()
def abrir_pagina_atualizacao_Avaliacao():
    print("Abrindo página de atualização de Avaliação")
    AvaliacaoAtualizar.atualizar_avaliacao()
def abrir_pagina_atualizacao_Jogo():
    print("Abrindo página de atualização de Jogo")
    JogoAtualizar.atualizar_jogo()
def abrir_pagina_atualizacao_Desenvolvedora():
    print("Abrindo página de atualização de Desenvolvedora")
    DesenvolvedoraAtualizar.atualizar_desenvolvedora()


def abrir_pagina_delete_Usuario():
    print("Abrindo página de exclusão de Usuário")
    UsuarioDelete.deletar_usuario()
def abrir_pagina_delete_Empresa():
    print("Abrindo página de exclusão de Empresa")
    EmpresaproprietariaDelete.deletar_empresa()
def abrir_pagina_delete_Avaliacao():
    print("Abrindo página de exclusão de Avaliação")
    AvaliacaoDelete.deletar_avaliacao()
def abrir_pagina_delete_Jogo():
    print("Abrindo página de exclusão de Jogo")
    JogoDelete.deletar_jogo()
def abrir_pagina_delete_Desenvolvedora():
    print("Abrindo página de exclusão de Desenvolvedora")
    DesenvolvedoraDelete.deletar_desenvolvedora()
# Configuração da janela principal
root = tk.Tk()
root.title("Sistema de Cadastro de Usuários")
root.geometry("320x560")  # Dimensão inicial da janela
root.resizable(False, True)  # Redimensionamento vertical permitido, mas não horizontal

# Estilo ttk
style = ttk.Style()
style.configure("TFrame", background="#f5f5f5")
style.configure("TButton", padding=6, relief="flat", background="#d9d9d9")
style.configure("TLabel", background="#f5f5f5")

# Função para criar a interface do menu
def criar_menu():
    # Frame principal
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky="NSEW")

    # Frame de Cadastro
    frame_cadastro = ttk.Labelframe(frame, text="Cadastro", padding="10")
    frame_cadastro.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="NSEW")

    ttk.Button(frame_cadastro, text="Usuário", command=abrir_pagina_cadastro_Usuario).grid(row=0, column=0, pady=2, sticky="EW")
    ttk.Button(frame_cadastro, text="Desenvolvedora", command=abrir_pagina_cadastro_Desenvolvedora).grid(row=1, column=0, pady=2, sticky="EW")
    ttk.Button(frame_cadastro, text="Empresa", command=abrir_pagina_cadastro_Empresa).grid(row=2, column=0, pady=2, sticky="EW")
    ttk.Button(frame_cadastro, text="Jogo", command=abrir_pagina_cadastro_Jogo).grid(row=3, column=0, pady=2, sticky="EW")
    ttk.Button(frame_cadastro, text="Avaliação", command=abrir_pagina_cadastro_Avaliacao).grid(row=4, column=0, pady=2, sticky="EW")

    # Frame de Listagem
    frame_listagem = ttk.Labelframe(frame, text="Listagem", padding="10")
    frame_listagem.grid(row=1, column=0, padx=10, pady=5, sticky="NSEW")

    ttk.Button(frame_listagem, text="Usuários", command=abrir_pagina_listagem_Usuario).grid(row=0, column=0, pady=2, sticky="EW")
    ttk.Button(frame_listagem, text="Desenvolvedoras", command=abrir_pagina_listagem_Desenvolvedora).grid(row=1, column=0, pady=2, sticky="EW")
    ttk.Button(frame_listagem, text="Empresas", command=abrir_pagina_listagem_Empresa).grid(row=2, column=0, pady=2, sticky="EW")
    ttk.Button(frame_listagem, text="Jogos", command=abrir_pagina_listagem_Jogo).grid(row=3, column=0, pady=2, sticky="EW")
    ttk.Button(frame_listagem, text="Avaliações", command=abrir_pagina_listagem_Avaliacao).grid(row=4, column=0, pady=2, sticky="EW")

    # Frame de Atualização
    frame_atualizacao = ttk.Labelframe(frame, text="Atualização", padding="10")
    frame_atualizacao.grid(row=0, column=1, padx=10, pady=(10, 5), sticky="NSEW")

    ttk.Button(frame_atualizacao, text="Usuário", command=abrir_pagina_atualizacao_Usuario).grid(row=0, column=0, pady=2, sticky="EW")
    ttk.Button(frame_atualizacao, text="Desenvolvedora", command=abrir_pagina_atualizacao_Desenvolvedora).grid(row=1, column=0, pady=2, sticky="EW")
    ttk.Button(frame_atualizacao, text="Empresa", command=abrir_pagina_atualizacao_Empresa).grid(row=2, column=0, pady=2, sticky="EW")
    ttk.Button(frame_atualizacao, text="Jogo", command=abrir_pagina_atualizacao_Jogo).grid(row=3, column=0, pady=2, sticky="EW")
    ttk.Button(frame_atualizacao, text="Avaliação", command=abrir_pagina_atualizacao_Avaliacao).grid(row=4, column=0, pady=2, sticky="EW")

    # Frame de Delete
    frame_delete = ttk.Labelframe(frame, text="Exclusão", padding="10")
    frame_delete.grid(row=1, column=1, padx=10, pady=5, sticky="NSEW")

    ttk.Button(frame_delete, text="Usuário", command=abrir_pagina_delete_Usuario).grid(row=0, column=0, pady=2, sticky="EW")
    ttk.Button(frame_delete, text="Desenvolvedora", command=abrir_pagina_delete_Desenvolvedora).grid(row=1, column=0, pady=2, sticky="EW")
    ttk.Button(frame_delete, text="Empresa", command=abrir_pagina_delete_Empresa).grid(row=2, column=0, pady=2, sticky="EW")
    ttk.Button(frame_delete, text="Jogo", command=abrir_pagina_delete_Jogo).grid(row=3, column=0, pady=2, sticky="EW")
    ttk.Button(frame_delete, text="Avaliação", command=abrir_pagina_delete_Avaliacao).grid(row=4, column=0, pady=2, sticky="EW")

# Chamar função para criar o menu
criar_menu()

# Loop principal da janela
root.mainloop()
