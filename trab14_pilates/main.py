#regras negocio
#

import tkinter as tk
import profissional
import aluno
#Lucas Melo


class ViewPrincipal():
    def __init__(self, root, controle):
        #configurando a view
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')

        #configurando o menu
        self.menubar = tk.Menu(self.root)        
        self.menu_profissional = tk.Menu(self.menubar)
        self.menu_aluno = tk.Menu(self.menubar)

        

        #profissional
        self.menu_profissional.add_command(label="Cadastra", \
                    command=self.controle.cadastrarProfissional)
        self.menu_profissional.add_command(label="Lista", \
                    command=self.controle.listarProfissionais)
        self.menubar.add_cascade(label="Profissinal", \
                    menu=self.menu_profissional)    
        
        self.menu_aluno.add_command(label="Cadastra", \
                    command=self.controle.cadastrarAluno)
        self.menu_aluno.add_command(label="Consultar", \
                    command=self.controle.consultarAluno)
        

        self.menubar.add_cascade(label="Aluno", \
                    menu=self.menu_aluno)   
        

        self.root.config(menu=self.menubar)




class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()
        self.controle_profissional = profissional.ControleProfissional(self)
        self.controle_aluno = aluno.ControleAluno(self)
       
        self.view = ViewPrincipal(self.root, self) 

        self.root.title("Sistema Pilates - Lucas Melo")
        # Inicia o mainloop
        self.root.mainloop()
       
    def cadastrarProfissional(self):
        self.controle_profissional.cadastrar_view()
    def listarProfissionais(self):
        self.controle_profissional.listar_profissionais_view()

    def cadastrarAluno(self):
        self.controle_aluno.cadastrar_view()
    def consultarAluno(self):
        self.controle_aluno.consultar_aluno_view()

if __name__ == '__main__':
    c = ControlePrincipal()