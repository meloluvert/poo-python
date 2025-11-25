import tkinter as tk
import artista
import album
import playlist
#Lucas Melo


class LimitePrincipal():
    def __init__(self, root, controle):
        #configurando a view
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')

        #configurando o menu
        self.menubar = tk.Menu(self.root)        
        self.menu_artista = tk.Menu(self.menubar)
        self.menu_album = tk.Menu(self.menubar)
        self.menu_playlist = tk.Menu(self.menubar)     

        #Artista
        self.menu_artista.add_command(label="Cadastrar", \
                    command=self.controle.cadastrarArtista)
        self.menu_artista.add_command(label="Consultar", \
                    command=self.controle.consultarArtistas)
        self.menubar.add_cascade(label="Artista", \
                    menu=self.menu_artista)    
        
        #Album
        self.menu_album.add_command(label="Cadastrar", \
                    command=self.controle.cadastrarAlbum)
        self.menu_album.add_command(label="Consultar", \
                    command=self.controle.consultarAlbuns)
        self.menubar.add_cascade(label="Albuns", \
                    menu=self.menu_album)   
        
        #Playlist
        self.menu_playlist.add_command(label="Cadastrar", \
                    command=self.controle.cadastrarPlaylist)
        self.menu_playlist.add_command(label="Consultar", \
                    command=self.controle.consultarPlaylists)
        self.menubar.add_cascade(label="Playlists", \
                    menu=self.menu_playlist)    

        self.root.config(menu=self.menubar)




class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.controle_artista = artista.ControleArtista(self)
        self.controle_album = album.ControleAlbum(self)
        self.controle_playlist = playlist.ControlePlaylist(self)
        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Spotify II - Lucas Melo")
        # Inicia o mainloop
        self.root.mainloop()
       
    def cadastrarArtista(self):
        self.controle_artista.cadastrar_view()
    def consultarArtistas(self):
        self.controle_artista.consultar_view()

    def cadastrarAlbum(self):
        self.controle_album.cadastrar_view()
    def consultarAlbuns(self):
        self.controle_album.consultar_view()


    def cadastrarPlaylist(self):
        self.controle_playlist.cadastrar_view()
    def consultarPlaylists(self):
        self.controle_playlist.consultar_view()

if __name__ == '__main__':
    c = ControlePrincipal()