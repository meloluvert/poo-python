import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog

class Artista:
    def __init__(self, nome):
        self.__nome = nome
        self.__albuns = []
        self.__musicas = []

    @property
    def nome(self):
        return self.__nome

    @property
    def albuns(self):
        return self.__albuns

    @property
    def musicas(self):
        return self.__musicas

    def addAlbum(self, album):
        self.__albuns.append(album)

    def addMusica(self, musica):
        self.__musicas.append(musica)
    
class ControleArtista():       
    def __init__(self, controle_principal):
        self.lista_artistas = []
        self.controle_principal = controle_principal

    def get_artista(self, nome):
        for artista in self.lista_artistas:
            if(artista.nome == nome):
                return artista

    def cadastrar_view(self):
        self.view_cadastrar = ViewCadastrarArtista(self) 

    def consultar_view(self):
        nome_artista = simpledialog.askstring("Consultar Artista", "Digite o nome do artista:")
        if nome_artista is not None and nome_artista.strip() != "":                
            self.view_mostrar = ViewMostraArtista(self.consultar(nome_artista))
    def consultar(self, nome):
        artista_encontrado = None
        for artista in self.lista_artistas:
            if(nome == artista.nome):
                artista_encontrado = artista 
        if(artista_encontrado is None):
            self.view_consultar = ViewMostraArtista("Artista não encontrado") 
        else:
            albuns = self.controle_principal.controle_album.get_albuns_por_artista(artista_encontrado)
            str ="Álbuns de " + artista_encontrado.nome +"\n"
            for album in albuns:
                str+= album.titulo +" -- " + album.ano +"\n"
                for musica in album.faixas:
                    str+= "  "+ musica.titulo +"\n"
            return str

    def limpar_input(self, event):
        self.view_cadastrar.input_nome.delete(0, len(self.view_cadastrar.input_nome.get()))

    def cadastrar(self, event):
        nome = self.view_cadastrar.input_nome.get()
        artista = Artista(nome)
        self.lista_artistas.append(artista)
        self.view_cadastrar.mostrar_janela('Sucesso', 'Artista cadastrado com sucesso')
        self.limpar_input(event)
        self.fechar_janela(event)

    def fechar_janela(self, event):
        self.view_cadastrar.destroy()


class ViewMostraArtista():
    def __init__(self, str):
        messagebox.showinfo('Lista de álbuns', str)
class ViewCadastrarArtista(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Artista")
        self.controle = controle

        self.frame_nome = tk.Frame(self)
        self.frame_botoes = tk.Frame(self)
        self.frame_nome.pack()
        self.frame_botoes.pack()


        self.label_nome = tk.Label(self.frame_nome,text="Nome: ")
        self.label_nome.pack(side="left")

        self.input_nome = tk.Entry(self.frame_nome,  width=20)
        self.input_nome.pack(side="left")

        #botoes
        self.botao_enviar = tk.Button(self.frame_botoes ,text="Cadastrar")      
        self.botao_enviar.pack(side="left")
        self.botao_enviar.bind("<Button>", controle.cadastrar)
      
        self.botao_limpar = tk.Button(self.frame_botoes ,text="Limpar")      
        self.botao_limpar.pack(side="left")
        self.botao_limpar.bind("<Button>", controle.limpar_input)  

        self.botao_fechar = tk.Button(self.frame_botoes ,text="Sair")      
        self.botao_fechar.pack(side="left")
        self.botao_fechar.bind("<Button>", controle.fechar_janela)
    def mostrar_janela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)