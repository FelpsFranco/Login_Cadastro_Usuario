import tkinter.ttk
from tkinter import *
import pygame
import os
from utils import obtendo_arquivos, stop_musica, play_musica, musica_tocando, pause_musica



class Music:
    def __init__(self, musicas, tocando=False):
        self.musicas = musicas
        self.tocando = tocando

    def incia(self):
        self.janela_inicial = Tk()
        self.janela_inicial.geometry('600x860+0+0')
        self.janela_inicial.resizable(width=False, height=False)
        self.janela_inicial.title('Bem Vindo')
        self.janela_inicial.configure(bg='gray15')

        pygame.init()
        pygame.mixer.init()


        self.proximo = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Imagens/prox.png')
        self.anterior = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Imagens/Ant.png')
        self.pause = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Imagens/pausa.png')
        self.iniciar = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Imagens/Play.png')
        self.musiquinha = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Imagens/album.png')



        self.button_prox = Button(self.janela_inicial,command=self.prox, image=self.proximo, borderwidth=0, bg='gray15', activebackground='gray15')
        self.button_prox.place(x=510, y=520)

        self.button_ant = Button(self.janela_inicial, command=self.ante, image=self.anterior, borderwidth=0, bg='gray15', activebackground='gray15')
        self.button_ant.place(x=20, y=520)

        self.button_play_music = Button(self.janela_inicial, image=self.iniciar, command=self.play, borderwidth=0, bg='gray15',activebackground='gray15')
        self.button_play_music.place(x=270, y=520)

        self.label_music = Label(self.janela_inicial, image=self.musiquinha, borderwidth=1, anchor=CENTER, bg='gray15')
        self.label_music.place(x=130, y=20)

        self.progress = tkinter.ttk.Progressbar(self.janela_inicial, maximum=100)
        self.progress.place(x=50, y=480, width=500, height=30)


        self.songframe = LabelFrame(self.janela_inicial, text='Playlist', font=("times new roman",15,"bold"), bg="gray15", fg="white", bd=0, relief=GROOVE, foreground='pink')
        self.songframe.place(x=10, y=600, width=580, height=150)

        scrol_y = Scrollbar(self.songframe, orient=VERTICAL)
        self.playlist = Listbox(self.songframe, yscrollcommand=scrol_y.set, selectbackground='purple4',selectmode=SINGLE, font=("times new roman", 12, "bold"), bg="gray15", fg="white", bd=0,relief=GROOVE)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill='both')

        os.chdir('C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Musicas')
        self.songtracks = os.listdir()
        for track in self.songtracks:
            self.playlist.insert(END, track)


        self.diretorio = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Musicas'
        self.musica_diretorio = obtendo_arquivos(self.diretorio)
        self.conta_musica = len(self.musica_diretorio)
        self.musica_index = 0

        self.janela_inicial.mainloop()

    def play(self):
        if self.tocando == False:
            self.tocando = True
            self.iniciar['file'] = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Imagens/pausa.png'
            if musica_tocando():
                pass
            if musica_tocando() == False:
                play_musica(self.musica_diretorio[self.musica_index])

        else:
            self.tocando = False
            self.iniciar['file'] = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Imagens/Play.png'
            if musica_tocando():
                pause_musica()
            pass

    def prox(self):
        if self.musica_index + 1 < self.conta_musica:
            stop_musica()
            self.musica_index += 1
            play_musica(self.musica_diretorio[self.musica_index])
        else:
            print('Reached last song')
            pass

    def ante(self):
        if self.musica_index + 1 <= self.conta_musica and self.musica_index > 0:
            stop_musica()
            self.musica_index -= 1
            play_musica(self.musica_diretorio[self.musica_index])
        else:
            print('Reached first song')




