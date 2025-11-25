import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog
import pickle
import os

class Produto:
    def __init__(self, codigo,descricao, valor):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = float(valor)
    @property
    def descricao(self):
        return self.__descricao

    @property
    def codigo(self):
        return self.__codigo

    @property
    def valor(self):
        return self.__valor

    
class ControleProduto():       

    def __init__(self, controle_principal):        
        if not os.path.isfile("produto.pickle"):
            self.lista_produtos = []
        else:
            with open("produto.pickle", "rb") as f:
                self.lista_produtos = pickle.load(f)
        self.controle_principal = controle_principal

    def get_produto(self, nome):
        for produto in self.lista_produtos:
            if(produto.descricao == nome):
                return produto

    def get_produtos(self):
        return self.lista_produtos
    def cadastrar_view(self):
        self.view_cadastrar = ViewCadastrarProduto(self) 

    def salvar_produtos(self):
        if len(self.lista_produtos) != 0:
            with open("produto.pickle","wb") as f:
                pickle.dump(self.lista_produtos, f)

    def consultar_view(self):
        descricao_produto = simpledialog.askstring("Consultar produto", "Digite o descricao do produto:")
        if descricao_produto is not None and descricao_produto.strip() != "":                
            self.view_mostrar = ViewMostraProduto(self.consultar(descricao_produto))
    def consultar(self, codigo):
        produto_encontrado = None
        for produto in self.lista_produtos:
            if(codigo == produto.codigo):
                produto_encontrado = produto 
        if(produto_encontrado is None):
            return "Produto não encontrado"
        else:
            texto = "Descrição:" + produto_encontrado.descricao +"\n"
            texto += "Valor: R$" + str(produto_encontrado.valor) + "\n"
            return texto

    def limpar_input(self, event):
        self.view_cadastrar.input_valor_unitario.delete(0, len(self.view_cadastrar.input_valor_unitario.get()))
        self.view_cadastrar.input_codigo.delete(0, len(self.view_cadastrar.input_codigo.get()))
        self.view_cadastrar.input_descricao.delete(0, len(self.view_cadastrar.input_descricao.get()))

    def cadastrar(self, event):
        codigo = self.view_cadastrar.input_codigo.get()
        descricao = self.view_cadastrar.input_descricao.get()
        valor = self.view_cadastrar.input_valor_unitario.get()

        produto = Produto(codigo, descricao, valor)
        self.lista_produtos.append(produto)
        self.view_cadastrar.mostrar_janela('Sucesso', 'Produto cadastrado com sucesso')
        self.salvar_produtos()
        self.limpar_input(event)
        self.fechar_janela(event)

    def fechar_janela(self, event):

        self.view_cadastrar.destroy()


class ViewMostraProduto():
    def __init__(self, str):
        messagebox.showinfo('Produto', str)
class ViewCadastrarProduto(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x500')
        self.title("Cadastro de Produtos")
        self.controle = controle


        self.frame_codigo = tk.Frame(self)
        self.frame_descricao = tk.Frame(self)
        self.frame_valor_unitario = tk.Frame(self)
        self.frame_botoes = tk.Frame(self)

        self.frame_codigo.pack()
        self.frame_descricao.pack()
        self.frame_valor_unitario.pack()
        self.frame_botoes.pack()


        self.label_descricao = tk.Label(self.frame_descricao,text="Descrição: ")
        self.label_descricao.pack(side="left")
        self.input_descricao = tk.Entry(self.frame_descricao,  width=20)
        self.input_descricao.pack(side="left")

        self.label_codigo = tk.Label(self.frame_codigo,text="Código: ")
        self.label_codigo.pack(side="left")
        self.input_codigo = tk.Entry(self.frame_codigo,  width=20)
        self.input_codigo.pack(side="left")

        self.label_valor_unitario = tk.Label(self.frame_valor_unitario,text="Valor Unitário: R$")
        self.label_valor_unitario.pack(side="left")
        self.input_valor_unitario = tk.Entry(self.frame_valor_unitario,  width=20)
        self.input_valor_unitario.pack(side="left")

        #botoes
        self.botao_enviar = tk.Button(self.frame_botoes ,text="Cadastrar")      
        self.botao_enviar.pack(side="left")
        self.botao_enviar.bind("<Button>", controle.cadastrar)
      
        self.botao_limpar = tk.Button(self.frame_botoes ,text="Limpar")      
        self.botao_limpar.pack(side="left")
        self.botao_limpar.bind("<Button>", controle.limpar_input)  

        self.botao_fechar = tk.Button(self.frame_botoes ,text="Sair")      
        self.botao_fechar.pack(side="left")
        self.botao_fechar.bind("<Button>", controle.fechar_janela)
    def mostrar_janela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)