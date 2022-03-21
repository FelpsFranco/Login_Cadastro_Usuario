from tkinter import *

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


        self.proximo = PhotoImage(file='Próximo.png')
        self.anterior = PhotoImage(file='Anterior.png')
        self.pause = PhotoImage(file='pause.png')
        self.musiquinha = PhotoImage(file='music1.png')

        self.button_prox = Button(self.janela_inicial, image=self.proximo, borderwidth=0, bg='gray15', activebackground='gray15')
        self.button_prox.place(x=470, y=600)

        self.button_ant = Button(self.janela_inicial, image=self.anterior, borderwidth=0, bg='gray15', activebackground='gray15')
        self.button_ant.place(x=70, y=600)

        self.button_play = Button(self.janela_inicial, image=self.pause, command=self.play, borderwidth=0, bg='gray15', activebackground='gray15')
        self.button_play.place(x=270, y=600)

        self.label_music = Label(self.janela_inicial, image=self.musiquinha, borderwidth=1, bg='black')
        self.label_music.place(x=120, y=100)


        self.janela_inicial.mainloop()


    def play(self):
        if self.tocando == False:
            self.tocando = True
            print('Tocando')


        else:
            self.tocando = False
            print('Pausado')



