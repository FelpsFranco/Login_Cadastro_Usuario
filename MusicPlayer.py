from tkinter import *
import pygame
import os

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
        self.track = StringVar()
        self.status = StringVar()

        self.proximo = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Imagens/Próximo.png')
        self.anterior = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Imagens/Anterior.png')
        self.pause = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Imagens/pause.png')
        self.musiquinha = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Imagens/music1.png')



        self.button_prox = Button(self.janela_inicial, image=self.proximo, borderwidth=0, bg='gray15', activebackground='gray15')
        self.button_prox.place(x=470, y=520)

        self.button_ant = Button(self.janela_inicial, image=self.anterior, borderwidth=0, bg='gray15', activebackground='gray15')
        self.button_ant.place(x=70, y=520)

        self.button_play = Button(self.janela_inicial, image=self.pause, command=self.play, borderwidth=0, bg='gray15', activebackground='gray15')
        self.button_play.place(x=270, y=520)

        self.label_music = Label(self.janela_inicial, image=self.musiquinha, borderwidth=1, bg='black')
        self.label_music.place(x=120, y=20)

        trackframe = LabelFrame(self.janela_inicial, text='Song Track', font=('times new roman',15,'bold'), bg='gray15',fg="white", relief=GROOVE)
        trackframe.place(x=30, y=450, width=500, height=70)

        songtrack = Label(trackframe, textvariable=self.track, width=27, font=('times new roman',15,'bold'),bg='gray15',fg='black')
        songtrack.grid(row=0,column=0, padx=30, pady=5)
        trackstatus = Label(trackframe, textvariable=self.status, font=("times new roman",15,"bold"),bg="gray15",fg="black")
        trackstatus.grid(row=0, column=1, padx=15, pady=5)

        self.songframe = LabelFrame(self.janela_inicial, text='Song Playlist', font=("times new roman",15,"bold"), bg="gray15", fg="white", bd=5, relief=GROOVE)
        self.songframe.place(x=10, y=600, width=580, height=100)

        scrol_y = Scrollbar(self.songframe, orient=VERTICAL)
        self.playlist = Listbox(self.songframe, yscrollcommand=scrol_y.set, selectbackground='purple4', selectmode=SINGLE, font=("times new roman",12,"bold"), bg="gray15", fg="white", bd=0, relief=GROOVE)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill='both')


        os.chdir('C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Musicas')
        self.songtracks = os.listdir()
        for track in self.songtracks:
            self.playlist.insert(END, track)

        self.janela_inicial.mainloop()


    def play(self):
        if self.tocando == False:
            self.tocando = True
            pygame.init()
            pygame.mixer.init()
            self.track.set(self.playlist.get(ACTIVE))
            self.status.set('-Playing')
            pygame.mixer.music.load(self.playlist.get(ACTIVE))
            pygame.mixer.music.play()

        else:
            self.tocando = False
            self.status.set('-Paused')
            pygame.mixer.music.pause()

    # def prox(self):
    #     musicas = []
    #     path = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/TelaLogin/Musicas'
    #     for item in os.listdir(path):
    #         if item.endswith('.mp3'):
    #             musicas.append(item)
    #     x = musicas.index(self.track.get())
    #     prox_musica = musicas[x+1]
    #     print(prox_musica)
    #     self.track.set(prox_musica)
    #     self.playlist.event_generate('<Button-1>', x=270, y=520)






