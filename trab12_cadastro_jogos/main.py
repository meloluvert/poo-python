import tkinter as tk
import jogo
#Lucas Melo


class ViewPrincipal():
    def __init__(self, root, controle):
        #configurando a view
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')

        #configurando o menu
        self.menubar = tk.Menu(self.root)        
        self.menu_jogo = tk.Menu(self.menubar)
        self.menu_cupom_fiscal = tk.Menu(self.menubar)

        #Jogo
        self.menu_jogo.add_command(label="Cadastrar", \
                    command=self.controle.cadastrarJogo)
        self.menu_jogo.add_command(label="Avaliar", \
                    command=self.controle.avaliarJogo)
        self.menu_jogo.add_command(label="Consultar", \
                    command=self.controle.consultarJogo)
        self.menubar.add_cascade(label="Jogo", \
                    menu=self.menu_jogo)    
        

        self.root.config(menu=self.menubar)




class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.controle_Jogo = jogo.ControleJogo(self)
       
        self.view = ViewPrincipal(self.root, self) 

        self.root.title("Cadastro de Jogos - Lucas Melo")
        # Inicia o mainloop
        self.root.mainloop()
       
    def cadastrarJogo(self):
        self.controle_Jogo.cadastrar_view()
    def consultarJogo(self):
        self.controle_Jogo.consultar_view()
    def avaliarJogo(self):
        self.controle_Jogo.avaliar_view()
        

if __name__ == '__main__':
    c = ControlePrincipal()