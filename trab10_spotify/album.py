import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import musica
import tkinter.simpledialog as simpledialog

class Album:
    def __init__(self, titulo, artista, ano):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano

        self.__faixas = []
        artista.addAlbum(self)

    @property
    def titulo(self):
        return self.__titulo

    @property
    def artista(self):
        return self.__artista

    @property
    def ano(self):
        return self.__ano

    @property
    def faixas(self):
        return self.__faixas

    def addFaixa(self, titulo, artista=None):
        if artista is None:
            artista = self.__artista
        nroFaixa = len(self.__faixas)
       
        self.__faixas.append(musica.Musica(titulo, artista, self, nroFaixa))

class ControleAlbum():       
    def __init__(self, controle_principal):
        self.lista_albuns = []
        self.controle_principal = controle_principal

    def cadastrar_view(self):
        lista_artistas = self.controle_principal.controle_artista.lista_artistas
        self.view_cadastrar_album = ViewCadastrarAlbum(self,lista_artistas)

    def consultar_view(self):
        nome_album = simpledialog.askstring("Consultar Álbum", "Digite o nome do álbum:")
        if nome_album is not None and nome_album.strip() != "":                
            self.view_mostrar = ViewMostraAlbum(self.consultar(nome_album))

    def consultar(self, nome):
        album_encontrado = None
        for album in self.lista_albuns:
            if(nome == album.titulo):
                album_encontrado = album
        if(album_encontrado is None):
            self.view_consultar = ViewMostraAlbum("Álbum não encontracdo") 
        else:
            str = "Músicas -- " + album_encontrado.titulo + " -- " + album_encontrado.ano +"\n"
            for musica in album_encontrado.faixas:
                str+= " - "+ musica.titulo +"\n"
            return str

    def limpar_input(self, event):
        self.view_cadastrar_album.input_titulo.delete(0, len(self.view_cadastrar_album.input_titulo.get()))
        self.view_cadastrar_album.input_ano.delete(0, len(self.view_cadastrar_album.input_ano.get()))

    def cadastrar(self, event):
        titulo = self.view_cadastrar_album.input_titulo.get()
        ano = self.view_cadastrar_album.input_ano.get()
        artista = self.controle_principal.controle_artista.get_artista(self.view_cadastrar_album.nome_artista_escolhido.get())
        album = Album(titulo, artista, ano)

        for nome_musica in self.view_cadastrar_album.lista_musicas:
            album.addFaixa(nome_musica)
        self.lista_albuns.append(album)
        self.view_cadastrar_album.mostrar_janela('Sucesso', 'Álbum cadastrado com sucesso')
        self.limpar_input(event)
        self.fechar_janela(event)

    def get_albuns_por_artista(self, artista):
        lista_albuns_artista = []
        for album in self.lista_albuns:
            if album.artista == artista:
                lista_albuns_artista.append(album)
        return lista_albuns_artista
                

    #chama o simple dialog
    def cadastrar_musica(self, event):
        nome_musica = simpledialog.askstring("Nova Música", "Digite o título da música:")
        if nome_musica is not None and nome_musica.strip() != "":
            if hasattr(self, 'view_cadastrar_album'):
                 self.view_cadastrar_album.adiciona_musica(nome_musica)
    def fechar_janela(self, event):
        self.view_cadastrar_album.destroy()

class ViewMostraAlbum():
    def __init__(self, str):
        messagebox.showinfo('Lista de músicas', str)
class ViewCadastrarAlbum(tk.Toplevel):
    def __init__(self, controle, lista_artistas):

        self.lista_musicas = []
        tk.Toplevel.__init__(self)
        self.geometry('300x500')
        self.title("Álbum")
        self.controle = controle


        self.frame_titulo = tk.Frame(self)
        self.frame_ano = tk.Frame(self)
        self.frame_artista = tk.Frame(self)
        self.frame_musicas = tk.Frame(self)
        self.frame_botoes = tk.Frame(self)

        self.frame_titulo.pack()
        self.frame_ano.pack()
        self.frame_artista.pack()
        self.frame_musicas.pack()
        self.frame_botoes.pack()        

        self.label_titulo = tk.Label(self.frame_titulo,text="Título: ")
        self.label_titulo.pack(side="left")
        self.input_titulo= tk.Entry(self.frame_titulo, width=20)
        self.input_titulo.pack(side="left")

        self.label_ano = tk.Label(self.frame_ano,text="Ano: ")
        self.label_ano.pack(side="left")
        self.input_ano= tk.Entry(self.frame_ano, width=20)
        self.input_ano.pack(side="left")

        self.label_artista = tk.Label(self.frame_artista,text="Artista: ")
        self.label_artista.pack(side="left")
        self.nome_artista_escolhido = tk.StringVar()
        self.combobox = ttk.Combobox(self.frame_artista, width = 15,textvariable = self.nome_artista_escolhido)
        self.combobox.pack(side="left")
        nomes_artistas = [artista.nome for artista in lista_artistas]
        self.combobox['values'] = nomes_artistas

        self.label_musicas = tk.Label(self.frame_musicas,text="Músicas do álbum: ")
        self.label_musicas.pack(side="top") 
        self.listbox = tk.Listbox(self.frame_musicas)
        self.listbox.pack(side="top")

        self.botao_inserir = tk.Button(self.frame_botoes ,text="Insere Música")           
        self.botao_inserir.pack(side="left")
        self.botao_inserir.bind("<Button>", controle.cadastrar_musica)

        self.botao_cadastrar = tk.Button(self.frame_botoes ,text="Cria Álbum")           
        self.botao_cadastrar.pack(side="left")
        self.botao_cadastrar.bind("<Button>", controle.cadastrar)    

    def adiciona_musica(self, nome_musica):
        self.lista_musicas.append(nome_musica)
        self.listbox.insert(tk.END, nome_musica) 
        messagebox.showinfo("Sucesso", f"Música '{nome_musica}' adicionada à lista temporária.")
    def mostrar_janela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)