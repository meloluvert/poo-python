import tkinter as tk
import produto
import cupom_fiscal
#Lucas Melo


class ViewPrincipal():
    def __init__(self, root, controle):
        #configurando a view
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')

        #configurando o menu
        self.menubar = tk.Menu(self.root)        
        self.menu_produto = tk.Menu(self.menubar)
        self.menu_cupom_fiscal = tk.Menu(self.menubar)

        #Produto
        self.menu_produto.add_command(label="Cadastrar", \
                    command=self.controle.cadastrarProduto)
        self.menu_produto.add_command(label="Consultar", \
                    command=self.controle.consultarProduto)
        self.menubar.add_cascade(label="Produto", \
                    menu=self.menu_produto)    
        
        #Cupom Fiscal
        self.menu_cupom_fiscal.add_command(label="Cadastrar", \
                    command=self.controle.cadastrarCupomFiscal)
        self.menu_cupom_fiscal.add_command(label="Consultar", \
                    command=self.controle.consultarCupomFiscal)
        self.menubar.add_cascade(label="Cupom Fical", \
                    menu=self.menu_cupom_fiscal)   

        self.root.config(menu=self.menubar)




class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.controle_produto = produto.ControleProduto(self)
        self.controle_cupom_fiscal = cupom_fiscal.ControleCupomFiscal(self)
        # self.controle_playlist = playlist.ControlePlaylist(self)
        self.view = ViewPrincipal(self.root, self) 

        self.root.title("Cupom Fiscal - Lucas Melo")
        # Inicia o mainloop
        self.root.mainloop()
       
    def cadastrarProduto(self):
        self.controle_produto.cadastrar_view()
    def consultarProduto(self):
        self.controle_produto.consultar_view()

    def cadastrarCupomFiscal(self):
        self.controle_cupom_fiscal.cadastrar_view()
        
    def consultarCupomFiscal(self):
        self.controle_cupom_fiscal.consultar_view()
        

if __name__ == '__main__':
    c = ControlePrincipal()