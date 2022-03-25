import tkinter.ttk
from tkinter import *
import pygame
import os
import youtube_dl

from utils import obtendo_arquivos, stop_musica, play_musica, musica_tocando, pause_musica



class Music:
    def __init__(self, musicas, tocando=False):
        self.musicas = musicas
        self.tocando = tocando

    def incia(self):
        self.janela_inicial = Tk()
        self.janela_inicial.geometry('600x600+0+0')
        self.janela_inicial.resizable(width=False, height=False)
        self.janela_inicial.title('Bem Vindo')
        self.janela_inicial.configure(bg='gray15')
        self.menubar = Menu(self.janela_inicial)
        self.janela_inicial.config(menu=self.menubar)
        self.file_menu = Menu(self.menubar)

        self.file_menu.add_command(label='Download', command=self.baixa)
        self.file_menu.add_command(label='Exit', command=self.janela_inicial.destroy)
        self.menubar.add_cascade(label='File', menu=self.file_menu, underline=0)

        pygame.init()
        pygame.mixer.init()


        self.proximo = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Imagens/prox.png')
        self.anterior = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Imagens/Ant.png')
        self.pause = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Imagens/pausa.png')
        self.iniciar = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Imagens/Play.png')
        self.album_utilizado = PhotoImage(file='')

        self.mostra_nome = Label(self.janela_inicial, text='', font=("times new roman", 12, "bold"), bg="gray15",fg="white", bd=0, relief=GROOVE, foreground='pink')
        self.mostra_nome.place(x=150, y=20, width=300, height=100)

        self.mostra_album = Label(self.janela_inicial, image=self.album_utilizado, borderwidth=0, bg='gray15')
        self.mostra_album.place(x=150, y=110)

        self.progress = tkinter.ttk.Progressbar(self.janela_inicial, maximum=100)
        self.progress.place(x=50, y=450, width=500, height=30)

        self.button_prox = Button(self.janela_inicial,command=self.prox, image=self.proximo, borderwidth=0, bg='gray15', activebackground='gray15')
        self.button_prox.place(x=400, y=500)

        self.button_play_music = Button(self.janela_inicial, image=self.iniciar, command=self.play, borderwidth=0,bg='gray15', activebackground='gray15')
        self.button_play_music.place(x=270, y=500)

        self.button_ant = Button(self.janela_inicial, command=self.ante, image=self.anterior, borderwidth=0, bg='gray15', activebackground='gray15')
        self.button_ant.place(x=120, y=500)



        # self.songframe = LabelFrame(self.janela_inicial, text='Playlist', font=("times new roman",15,"bold"), bg="gray15", fg="white", bd=0, relief=GROOVE, foreground='pink')
        # self.songframe.place(x=10, y=670, width=580, height=150)

        # scrol_y = Scrollbar(self.songframe, orient=VERTICAL)
        # self.playlist = Listbox(self.songframe, yscrollcommand=scrol_y.set, selectbackground='purple4', selectmode=SINGLE, font=("times new roman", 12, "bold"), bg="gray15", fg="white", bd=0, relief=GROOVE)
        # scrol_y.pack(side=RIGHT, fill=Y)
        # scrol_y.config(command=self.playlist.yview)
        # self.playlist.pack(fill='both')

        # os.chdir('C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Musicas')
        # self.songtracks = os.listdir()
        # for track in self.songtracks:
        #     self.playlist.insert(END, track)


        self.diretorio = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Musicas'
        self.musica_diretorio = obtendo_arquivos(self.diretorio)
        self.conta_musica = len(self.musica_diretorio)
        self.musica_index = 0

        self.diretorio_album = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Albuns'
        self.albuns_diretorio = obtendo_arquivos(self.diretorio_album)
        self.conta_album = len(self.albuns_diretorio)
        self.album_index = 0

        self.janela_inicial.mainloop()

    def atualiza_nome(self):
        self.mostra_nome['text'] = os.path.basename(self.musica_diretorio[self.musica_index])

    def play(self):
        if self.tocando == False:
            self.tocando = True
            self.iniciar['file'] = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Imagens/pausa.png'
            if musica_tocando():
                pass
            if musica_tocando() == False:
                play_musica(self.musica_diretorio[self.musica_index])
                self.album_utilizado['file'] = self.albuns_diretorio[self.album_index]
                self.atualiza_nome()

        else:
            self.tocando = False
            self.iniciar['file'] = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Imagens/Play.png'
            if musica_tocando():
                pause_musica()
            pass

    def prox(self):
        if self.tocando == False:
            self.tocando = True
            self.iniciar['file'] = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Imagens/pausa.png'
        if self.musica_index + 1 < self.conta_musica:
            stop_musica()
            self.musica_index += 1
            self.album_index += 1
            play_musica(self.musica_diretorio[self.musica_index])
            self.album_utilizado['file'] = self.albuns_diretorio[self.album_index]
            self.atualiza_nome()
        else:
            self.mensagem_erro_ultima()
            pass

    def ante(self):
        if self.musica_index + 1 <= self.conta_musica and self.musica_index > 0:
            stop_musica()
            self.musica_index -= 1
            self.album_index -= 1
            play_musica(self.musica_diretorio[self.musica_index])
            self.album_utilizado['file'] = self.albuns_diretorio[self.album_index]
            self.atualiza_nome()
        else:
            self.mensagem_erro_primeira()

    def mensagem_erro_ultima(self):
        self.mensagem = Tk()
        self.mensagem.geometry('300x100+50+250')
        self.mensagem.resizable(width=False, height=False)
        self.mensagem.configure(bg='black')
        self.mensagem.title('Erro')

        label_erro = Label(self.mensagem, image="::tk::icons::question", bg='black')
        label_erro.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
        label_mensagem = Label(self.mensagem, text="Você Chegou a última Música", bg='black', fg='white')
        label_mensagem.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")

        b1 = Button(self.mensagem, text="OK", command=self.mensagem.destroy, width=4, bg='white', borderwidth=0)
        b1.grid(row=1, column=1, padx=(35, 35), sticky="e")

    def mensagem_erro_primeira(self):
        self.mensagem = Tk()
        self.mensagem.geometry('300x100+50+250')
        self.mensagem.resizable(width=False, height=False)
        self.mensagem.focus_force()
        self.mensagem.grab_set()
        self.mensagem.configure(bg='black')
        self.mensagem.title('Erro')

        label_erro = Label(self.mensagem, image="::tk::icons::question", bg='black')
        label_erro.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
        label_mensagem = Label(self.mensagem, text="Esta é a primeira Música", bg='black', fg='white')
        label_mensagem.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")

        b1 = Button(self.mensagem, text="OK", command=self.mensagem.destroy, width=4, bg='white', borderwidth=0)
        b1.grid(row=1, column=1, padx=(35, 35), sticky="e")


    def baixa(self):
        self.janela_dow = Tk()
        self.janela_dow.geometry('400x300+0+0')
        self.janela_dow.resizable(width=False, height=False)
        self.janela_dow.title('Download')
        self.janela_dow.configure(bg='gray15')


        self.label_baixa = Label(self.janela_dow, text='Digite o Link do YouTube', fg='black', bg='white')
        self.label_baixa.place(x=10, y=40)
        self.video_url = Entry(self.janela_dow, fg='black', bg='white', borderwidth=1,  font=('italic', 12))
        self.video_url.place(x=10, y=70, width=350, height=28)
        b1 = Button(self.janela_dow, text="OK", command=self.baixando, width=4, bg='white', borderwidth=0)
        b1.place(x=50, y=110)


    def baixando(self):
        print(self.video_url.get())
        self.video_info = self.video_url.get()
        self.video_info = youtube_dl.YoutubeDL().extract_info(url=self.video_url, download=False)
        print(self.video_info)

        PATH = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Musicas'

        filename = 'PATH%(title)s'+'.mp3'
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': filename,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }]

        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([self.video_url.get()])
        self.janela_dow.destroy()