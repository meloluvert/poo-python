import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.simpledialog as simpledialog

class Pizza:
    def __init__(self, codigo, descricao, preco):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco = preco

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def preco(self):
        return self.__preco

    def __str__(self):
        return f"{self.descricao} - R$ {self.preco:.2f}"

class ViewCadastraPizza(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('300x200')
        self.title("Cadastro de Pizza")
        self.controle = controle

        self.frame_codigo = tk.Frame(self)
        self.frame_descricao = tk.Frame(self)
        self.frame_preco = tk.Frame(self)
        self.frame_botoes = tk.Frame(self)

        self.frame_codigo.pack()
        self.frame_descricao.pack()
        self.frame_preco.pack()
        self.frame_botoes.pack()

        tk.Label(self.frame_codigo, text="Código: ").pack(side="left")
        self.input_codigo = tk.Entry(self.frame_codigo, width=20)
        self.input_codigo.pack(side="left")

        tk.Label(self.frame_descricao, text="Descrição: ").pack(side="left")
        self.input_descricao = tk.Entry(self.frame_descricao, width=20)
        self.input_descricao.pack(side="left")

        tk.Label(self.frame_preco, text="Preço: ").pack(side="left")
        self.input_preco = tk.Entry(self.frame_preco, width=20)
        self.input_preco.pack(side="left")

        self.botao_cadastrar = tk.Button(self.frame_botoes, text="Cadastrar")
        self.botao_cadastrar.pack(side="left")
        self.botao_cadastrar.bind("<Button>", controle.cadastrar)

        self.botao_fechar = tk.Button(self.frame_botoes, text="Fechar")
        self.botao_fechar.pack(side="left")
        self.botao_fechar.bind("<Button>", lambda e: self.destroy())

    def mostrar_janela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class ControlePizza():
    def __init__(self, controle_principal):
        self.controle_principal = controle_principal
        self.pizzas = {}
        self.carregar_pizzas_iniciais()

    def carregar_pizzas_iniciais(self):
        iniciais = [
            (101, "Portuguesa", 65.00),
            (102, "Calabresa", 55.00),
            (103, "Lombinho", 60.00),
            (104, "Quatro queijos", 58.00),
            (105, "Marguerita", 52.00),
            (106, "Napolitana", 54.00),
        ]
        for cod, desc, preco in iniciais:
            self.pizzas[cod] = Pizza(cod, desc, preco)

    def get_pizza(self, codigo):
        return self.pizzas.get(codigo)

    def cadastrar_view(self):
        self.view_cadastrar = ViewCadastraPizza(self)

    def cadastrar(self, event):
        try:
            codigo = int(self.view_cadastrar.input_codigo.get())
            descricao = self.view_cadastrar.input_descricao.get().strip()
            preco = float(self.view_cadastrar.input_preco.get())

            if codigo in self.pizzas:
                messagebox.showerror("Erro", "Código já existe!")
                return
            if not descricao:
                messagebox.showerror("Erro", "Descrição obrigatória!")
                return

            self.pizzas[codigo] = Pizza(codigo, descricao, preco)
            self.view_cadastrar.mostrar_janela("Sucesso", "Pizza cadastrada!")
            
            self.view_cadastrar.input_codigo.delete(0, tk.END)
            self.view_cadastrar.input_descricao.delete(0, tk.END)
            self.view_cadastrar.input_preco.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Erro", "Dados inválidos!")

    def consultar_view(self):
        codigo_str = simpledialog.askstring("Consultar Pizza", "Digite o código da pizza:")
        if codigo_str is None:
            return
        try:
            codigo = int(codigo_str)
            pizza = self.get_pizza(codigo)
            if pizza:
                messagebox.showinfo("Pizza encontrada", str(pizza))
            else:
                messagebox.showinfo("Erro", "Pizza não encontrada!")
        except ValueError:
            messagebox.showerror("Erro", "Código inválido!")