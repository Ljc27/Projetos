import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import font
from tkinter import PhotoImage
import random

# definindo funções do jogo
def play_game():
    print("Jogo iniciado")

# Criando a janela 
janela = tk.Tk()
# Título do jogo
janela.title("Memory game")
# ESSA PARTE DE BAIXO É RELACIONADO AO JOGO MESMO, SO UMAS PARTES QUE É MAIS DA COR, FONTE E ETC
# definindo as configurações do jogo
num_linhas = 4
num_colunas = 4
cartao_size_w = 10
cartao_size_h = 5
cores_cartao = ['red', 'blue', 'cyan', 'green', 'yellow', 'purple', 'orange', 'margenta']
cor_fundo = "#000000"
cor_letra = "#ffffff"
cor_fonte = ('Arial', 26, 'bold italic')
maximo_tentativas = 10
fonte_helvica = ("Helvica", 16, "bold italic")


# Ícone da janela
icon = PhotoImage(file="icone_da_janela.png")
janela.iconphoto(True, icon)  
janela.configure(bg=cor_fundo)
janela.geometry("640x480")

# imagem fundo
imagem_fundo = ImageTk.PhotoImage(Image.open("imagem.png"))
background_label = tk.Label(janela, image=imagem_fundo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Label do titulo
titulo_label = tk.Label(janela, text="Memory Game", font=cor_fonte,
                        fg=cor_letra, bg=cor_fundo)
titulo_label.pack(pady=40)

# Criando botões iniciais

# Botão de play
botao_play= tk.Button(janela, text="Play", command=play_game(),background='green',highlightbackground='black',padx=40,anchor="center", font=fonte_helvica)
botao_play.pack(pady=10)

# Botão de quit
botao_quit = tk.Button(janela, text="Quit", command=janela.quit, background='red', highlightbackground='black',padx=40,font=fonte_helvica)
botao_quit.pack(pady=10)
# Abrindo janela 
janela.mainloop()
