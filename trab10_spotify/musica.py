class Musica:
    def __init__(self, titulo, artista, album, nroFaixa):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        self.__nroFaixa = nroFaixa

        artista.addMusica(self)

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def artista(self):
        return self.__artista

    @property
    def album(self):
        return self.__album

    @property
    def nroFaixa(self):
        return self.__nroFaixa
    
class ControleMusica():       
    def __init__(self):
        self.lista_musicas = []

    def cadastrar(self):
        pass

    def consultar(self):
        pass