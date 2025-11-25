#Lucas Melo dos Santos Miranda 
import tkinter as tk
import tkinter.simpledialog as simpledialog
from tkinter import messagebox

class ModelCliente():
    def __init__(self, nome, email, codigo):
        self.__nome = nome
        self.__email = email
        self.__codigo = codigo

    @property
    def codigo(self):
        return self.__codigo
    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

class View():
    def __init__(self, master, controller):
        self.controller = controller
        self.janela = tk.Frame(master)
        self.janela.pack()
        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame3 = tk.Frame(self.janela)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
      
        self.labelInfo1 = tk.Label(self.frame1,text="Nome: ")
        self.labelInfo2 = tk.Label(self.frame2,text="Email: ")
        self.labelInfo3 = tk.Label(self.frame3,text="Codigo: ")
        self.labelInfo1.pack(side="left")
        self.labelInfo2.pack(side="left")  
        self.labelInfo3.pack(side="left")  

        self.inputText1 = tk.Entry(self.frame1, width=20)
        self.inputText1.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=20)
        self.inputText2.pack(side="left")    
        self.inputText3 = tk.Entry(self.frame3, width=20)
        self.inputText3.pack(side="left")                      
      

        self.buttonSubmit = tk.Button(self.janela,text="Salva")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.salvaHandler)
      
        self.buttonClear = tk.Button(self.janela,text="Limpa")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler)   

        self.buttonShow = tk.Button(self.janela,text="Mostrar Cadastrados")      
        self.buttonShow.pack(side="left")
        self.buttonShow.bind("<Button>", controller.mostraClientes)        

        self.buttonShow = tk.Button(self.janela,text="Consultar por código")      
        self.buttonShow.pack(side="left")
        self.buttonShow.bind("<Button>", controller.consultaClienteHandler)            


    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class LimiteMostraClientes():
    def __init__(self, str):
        messagebox.showinfo('Lista de clientes', str)

class Controller():       
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x100')
        self.listaClientes = []

        # Cria a view passando referência da janela principal e
        # de si próprio (controlador)
        self.view = View(self.root, self) 

        self.root.title("Exemplo MVC")
        # Inicia o mainloop
        self.root.mainloop()

    def mostraClientes(self, event):
        str = 'Nome -- Email -- Código\n'
        for cliente in self.listaClientes:
            str += cliente.nome + ' -- ' + cliente.email + ' -- ' + cliente.codigo + '\n'
        self.limiteLista = LimiteMostraClientes(str)
    def salvaHandler(self, event):
        nomeCli = self.view.inputText1.get()
        emailCli = self.view.inputText2.get()
        codigoCLi = self.view.inputText3.get()
        cliente = ModelCliente(nomeCli, emailCli, codigoCLi)
        self.listaClientes.append(cliente)
        self.view.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
        self.clearHandler(event)

    def consultaClienteHandler(self,event):
        codigo_digitado = tk.simpledialog.askstring("Consulta de Cliente", "Digite o código do Cliente")
        cliente_encontrado = None
        for cliente in self.listaClientes:
            if(cliente.codigo == codigo_digitado):
                cliente_encontrado = cliente
                break
        if(cliente_encontrado is None):
             self.view.mostraJanela('Erro', 'Código não encontrado')
        str = 'Nome -- Email -- Código\n'
        str += cliente_encontrado.nome + ' -- ' + cliente_encontrado.email + ' -- ' + cliente_encontrado.codigo + '\n'
        self.limiteLista = LimiteMostraClientes(str)


    def clearHandler(self, event):
        self.view.inputText1.delete(0, len(self.view.inputText1.get()))
        self.view.inputText2.delete(0, len(self.view.inputText2.get())) 
        self.view.inputText3.delete(0, len(self.view.inputText3.get())) 

if __name__ == '__main__':
    c = Controller()