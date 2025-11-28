import tkinter as tk
import medico
import consulta
#Lucas Melo


class ViewPrincipal():
    def __init__(self, root, controle):
        #configurando a view
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')

        #configurando o menu
        self.menubar = tk.Menu(self.root)        
        self.menu_medico = tk.Menu(self.menubar)
        self.menu_consulta = tk.Menu(self.menubar)

        #medico
        self.menu_medico.add_command(label="Cadastrar", \
                    command=self.controle.cadastrarMedico)
        self.menu_medico.add_command(label="ListarConsultas", \
                    command=self.controle.listarConsultasMedico)
        self.menubar.add_cascade(label="Médico", \
                    menu=self.menu_medico)    
        
        self.menu_consulta.add_command(label="Cadastrar", \
                    command=self.controle.cadastrarConsulta)
        self.menubar.add_cascade(label="Consulta", \
                    menu=self.menu_consulta)   
        

        self.root.config(menu=self.menubar)




class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.controle_medico = medico.ControleMedico(self)
        self.controle_consulta = consulta.ControleConsulta(self)
       
        self.view = ViewPrincipal(self.root, self) 

        self.root.title("Sistema Médico - Lucas Melo")
        # Inicia o mainloop
        self.root.mainloop()
       
    def cadastrarMedico(self):
        self.controle_medico.cadastrar_view()
    def listarConsultasMedico(self):
        self.controle_consulta.listar_consultas_view()

    def cadastrarConsulta(self):
        self.controle_consulta.cadastrar_view()
        

if __name__ == '__main__':
    c = ControlePrincipal()