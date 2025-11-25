import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog
import musica

class Playlist:
    def __init__(self, nome):
        self.__nome = nome
        self.__musicas = []

    @property
    def nome(self):
        return self.__nome

    @property
    def musicas(self):
        return self.__musicas

    def addMusica(self, musica):
        if musica not in self.__musicas:
            self.__musicas.append(musica)

class ControlePlaylist:
    def __init__(self, controle_principal):
        self.__lista_playlists = []
        self.__controle_principal = controle_principal

    def cadastrar_view(self):
        lista_artistas = self.__controle_principal.controle_artista.lista_artistas
        self.__view_cadastrar_playlist = ViewCadastrarPlaylist(self, lista_artistas)

    def cadastrar(self, event):
        nome_playlist = self.__view_cadastrar_playlist.input_nome.get()

        if nome_playlist.strip() == "":
            messagebox.showerror("Erro", "O nome da playlist não pode estar vazio.")
            return

        playlist = Playlist(nome_playlist)

        for musica in self.__view_cadastrar_playlist.lista_musicas:
            playlist.addMusica(musica)

        self.__lista_playlists.append(playlist)
        self.__view_cadastrar_playlist.mostrar_janela("Sucesso", "Playlist cadastrada com sucesso!")
        self.__view_cadastrar_playlist.destroy()

    def consultar_view(self):
        nome_playlist = simpledialog.askstring("Consultar Playlist", "Digite o nome da playlist:")
        if nome_playlist is not None and nome_playlist.strip() != "":
            playlist = self.consultar(nome_playlist)
            if playlist is None:
                self.__view_mostra = ViewMostraPlaylist("Playlist não encontrada.")
            else:
                str_playlist = f"Playlist: {playlist.nome}\n\nMúsicas:\n"
                for musica in playlist.musicas:
                    str_playlist += f" - {musica.titulo} ({musica.artista.nome})\n"
                self.__view_mostra = ViewMostraPlaylist(str_playlist)

    def consultar(self, nome):
        for playlist in self.__lista_playlists:
            if playlist.nome == nome:
                return playlist
        return None

    def atualizar_listbox(self, event):
        nome_artista = self.__view_cadastrar_playlist.nome_artista_escolhido.get()
        artista = self.__controle_principal.controle_artista.get_artista(nome_artista)
        self.__view_cadastrar_playlist.atualizar_musicas(artista)

    def selecionar_musica(self, event):
        listbox = event.widget
        indice = listbox.curselection()
        if indice:
            nome_musica = listbox.get(indice)
            for artista in self.__controle_principal.controle_artista.lista_artistas:
                for album in artista.albuns:
                    for musica_obj in album.faixas:
                        if musica_obj.titulo == nome_musica:
                            self.__view_cadastrar_playlist.adiciona_musica(musica_obj)

class ViewCadastrarPlaylist(tk.Toplevel):
    def __init__(self, controle, lista_artistas):
        tk.Toplevel.__init__(self)
        self.geometry("400x350")
        self.title("Cadastrar Playlist")

        self.controle = controle
        self.lista_artistas = lista_artistas
        self.lista_musicas = []

        self.frame_nome = tk.Frame(self)
        self.frame_artista = tk.Frame(self)
        self.frame_listas = tk.Frame(self)
        self.frame_botoes = tk.Frame(self)

        self.frame_nome.pack()
        self.frame_artista.pack()
        self.frame_listas.pack()
        self.frame_botoes.pack()

        self.label_nome = tk.Label(self.frame_nome, text="Nome da Playlist: ")
        self.label_nome.pack(side="left")
        self.input_nome = tk.Entry(self.frame_nome, width=25)
        self.input_nome.pack(side="left")

        self.label_artista = tk.Label(self.frame_artista, text="Artista: ")
        self.label_artista.pack(side="left")
        self.nome_artista_escolhido = tk.StringVar()
        self.combobox_artista = ttk.Combobox(self.frame_artista, width=20, textvariable=self.nome_artista_escolhido)
        self.combobox_artista.pack(side="left")

        nomes_artistas = [artista.nome for artista in lista_artistas]
        self.combobox_artista["values"] = nomes_artistas
        self.combobox_artista.bind("<<ComboboxSelected>>", controle.atualizar_listbox)

        self.frame_esq = tk.Frame(self.frame_listas)
        self.frame_dir = tk.Frame(self.frame_listas)
        self.frame_esq.pack(side="left", padx=10)
        self.frame_dir.pack(side="left", padx=10)

        self.label_musicas = tk.Label(self.frame_esq, text="Músicas do artista:")
        self.label_musicas.pack()
        self.listbox_musicas = tk.Listbox(self.frame_esq, width=30, height=10)
        self.listbox_musicas.pack()
        self.listbox_musicas.bind("<<ListboxSelect>>", controle.selecionar_musica)

        self.label_playlist = tk.Label(self.frame_dir, text="Músicas da playlist:")
        self.label_playlist.pack()
        self.listbox_playlist = tk.Listbox(self.frame_dir, width=30, height=10)
        self.listbox_playlist.pack()

        self.botao_cadastrar = tk.Button(self.frame_botoes, text="Criar Playlist")
        self.botao_cadastrar.pack(pady=5)
        self.botao_cadastrar.bind("<Button>", controle.cadastrar)

    def atualizar_musicas(self, artista):
        self.listbox_musicas.delete(0, tk.END)
        for album in artista.albuns:
            for musica in album.faixas:
                self.listbox_musicas.insert(tk.END, musica.titulo)

    def adiciona_musica(self, musica_obj):
        if musica_obj not in self.lista_musicas:
            self.lista_musicas.append(musica_obj)
            self.listbox_playlist.insert(tk.END, musica_obj.titulo)
            messagebox.showinfo("Sucesso", f"Música '{musica_obj.titulo}' adicionada à playlist.")

    def mostrar_janela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class ViewMostraPlaylist:
    def __init__(self, str_msg):
        messagebox.showinfo("Playlist", str_msg)
