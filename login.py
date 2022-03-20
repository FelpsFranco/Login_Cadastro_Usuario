from tkinter import *

class Login:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('400x600+0+0')
        self.root.resizable(width=False, height=False)
        self.root.title('TELA LOGIN')
        self.root.config(cursor='hand1')
        self.root.configure(bg='gray15')
        login_user = PhotoImage(file='User.png')
        usuario_image = PhotoImage(file='Usuario.png')
        senha_image = PhotoImage(file='senha.png')
        linha = PhotoImage(file='Linha.png')


        self.label0 = Label(self.root, image=login_user, bg='gray15')
        self.label0.place(x=140, y=40)

        self.label_usuario = Label(self.root, image=usuario_image, borderwidth=0, bg='gray15')
        self.label_usuario.place(x=70, y=190)
        self.login_usuario = Entry(self.root, fg='black', bg='gray35', borderwidth=1, font=('italic', 12))
        self.login_usuario.place(x=110, y=192, width=205, height=28)

        self.label_senha = Label(self.root, image=senha_image, bg='gray15', borderwidth=0)
        self.label_senha.place(x=70, y=242)
        self.login_senha = Entry(self.root, fg='white', bg='gray35', borderwidth=1, show='*',  font=('italic', 12))
        self.login_senha.place(x=110, y=245, width=205, height=28)

        self.op2 = Button(self.root, text='ENTRAR',command=self.loginBackEnd, relief='solid', borderwidth=0, activebackground='purple4', fg='black', bg='purple4')
        self.op2.place(x=85, y=310, width=230, height=25)

        self.label3 = Label(self.root, text='Ou', width=9, height=1, fg='white', bg='gray15')
        self.label3.place(x=165, y=400)

        self.label4 = Label(self.root, image=linha, width=110, height=1)
        self.label4.place(x=70, y=409)
        self.label4 = Label(self.root, image=linha, width=115, height=1)
        self.label4.place(x=213, y=409)

        # ---------------------------------------------------------------------------------------------------------------------------#

        self.op1 = Button(self.root, text='CADASTRAR', command=self.solicita_cadastro, borderwidth=0, activebackground='purple4', relief='solid', fg='black', bg='purple4')
        self.op1.place(x=85, y=500, width=230, height=25)

        self.root.mainloop()

    def verifica_login(self):
        usuario_correto = 'admin'
        senha_correta = '1234'
        if self.usuario.get() == 'admin' and self.senha.get() == '1234':
            print('logado')
            self.root.destroy()
        else:
            print('Dados Incorretos!!')

    def solicita_cadastro(self):
        print('Iniciando Cadastro')
        self.root.destroy()
        self.cadastro()

    def cadastro(self):
        self.janela = Tk()
        self.janela.geometry('400x600+0+0')
        self.janela.resizable(width=False, height=False)
        self.janela.title('Cadastro de Usuário')
        self.janela.config(cursor='hand1')
        self.janela.configure(bg='gray15')
        new_user = PhotoImage(file='new_user.png')

        self.label0 = Label(self.janela, image=new_user,  borderwidth=0, bg='gray15')
        self.label0.place(x=140, y=40)

        self.label_usuario = Label(self.janela, text='Nome:', borderwidth=0, fg='white', bg='gray15', font=('italic', 12))
        self.label_usuario.place(x=55, y=195)
        self.usuario = Entry(self.janela, fg='black', bg='gray35', borderwidth=1, font=('italic', 12))
        self.usuario.place(x=110, y=192, width=205, height=28)

        self.label_senha = Label(self.janela, text='Senha:', fg='white', bg='gray15', borderwidth=0, font=('italic', 12))
        self.label_senha.place(x=55, y=250)
        self.senha = Entry(self.janela, fg='white', bg='gray35', borderwidth=1, show='*',  font=('italic', 12))
        self.senha.place(x=110, y=245, width=205, height=28)

        self.label_email = Label(self.janela, text='E-mail:', borderwidth=0,fg='white', bg='gray15', font=('italic', 12))
        self.label_email.place(x=55, y=305)
        self.email = Entry(self.janela, fg='black', bg='gray35', borderwidth=1, font=('italic', 12))
        self.email.place(x=110, y=298, width=205, height=28)

        self.op1 = Button(self.janela, text='SALVAR',command=self.cadastrarBackEnd, borderwidth=0, activebackground='purple4', relief='solid', fg='black', bg='purple4')
        self.op1.place(x=35, y=400, width=120, height=25)

        self.op2 = Button(self.janela, text='VOLTAR', command=self.volta_login, borderwidth=0, activebackground='purple4', relief='solid', fg='black', bg='purple4')
        self.op2.place(x=250, y=400, width=130, height=25)

        self.root.mainloop()



    def logado(self):
        self.janela_inicial = Tk()
        self.janela_inicial.geometry('863x860+0+0')
        self.janela_inicial.resizable(width=False, height=False)
        self.janela_inicial.title('Bem Vindo')
        imagem = PhotoImage(file='bemvindo.png')
        label0 = Label(self.janela_inicial, image=imagem)
        label0.place(x=0, y=0)

        self.janela_inicial.mainloop()



    def volta_login(self):
        self.janela.destroy()
        self.__init__()

    def cadastrarBackEnd(self):
        try:
            with open('usuarios.txt', 'a') as arquivoUsuario:
                arquivoUsuario.write(self.usuario.get() + '\n')

            with open('senhas.txt', 'a') as arquivoUsuario:
                arquivoUsuario.write(self.senha.get() + '\n')

            with open('Email.txt', 'a') as arquivoUsuario:
                arquivoUsuario.write(self.email.get() + '\n')
                self.janela.destroy()
                self.__init__()
        except:
            print('ERRO 404')

    def loginBackEnd(self):
        with open('usuarios.txt', 'r') as arquivoUsuario:
            usuarios = arquivoUsuario.readlines()

        with open('senhas.txt', 'r') as arquivoUsuario:
            senhas = arquivoUsuario.readlines()

        usuarios = list(map(lambda x: x.replace('\n', ''), usuarios))
        senhas = list(map(lambda x: x.replace('\n', ''), senhas))

        usuario = self.login_usuario.get()
        senha = self.login_senha.get()

        logado = False

        for i in range(len(usuarios)):
            if usuario == usuarios[i] and senha == senhas[i]:
                print('Usuário Logado')
                logado = True
                self.root.destroy()
                self.logado()

        if not logado:
            print('Usuário ou Senha Incorreto!!')

Login()