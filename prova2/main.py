import tkinter as tk
import pizza
import pedido

class ViewPrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('400x300')

        self.menubar = tk.Menu(self.root)        
        self.menu_pizza = tk.Menu(self.menubar)
        self.menu_pedido = tk.Menu(self.menubar)

        # Menu Pizza
        self.menu_pizza.add_command(label="Cadastrar", command=self.controle.cadastrarPizza)
        self.menu_pizza.add_command(label="Consultar", command=self.controle.consultarPizza)
        self.menubar.add_cascade(label="Pizzas", menu=self.menu_pizza)    
        
        # Menu Pedido
        self.menu_pedido.add_command(label="Cadastrar", command=self.controle.cadastrarPedido)
        self.menu_pedido.add_command(label="Consultar", command=self.controle.consultarPedido)
        self.menubar.add_cascade(label="Pedido", menu=self.menu_pedido)   

        self.root.config(menu=self.menubar)

class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()
        self.controle_pizza = pizza.ControlePizza(self)
        self.controle_pedido = pedido.ControlePedido(self)
       
        self.view = ViewPrincipal(self.root, self) 

        self.root.title("Pizzaria Mama Mia")
        self.root.mainloop()
       
    def cadastrarPizza(self):
        self.controle_pizza.cadastrar_view()
    def consultarPizza(self):
        self.controle_pizza.consultar_view()

    def cadastrarPedido(self):
        self.controle_pedido.cadastrar_view()
    def consultarPedido(self):
        self.controle_pedido.consultar_view()

if __name__ == '__main__':
    c = ControlePrincipal()