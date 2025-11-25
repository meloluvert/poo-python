import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.simpledialog as simpledialog
import pickle
import os
import math

class Jogo:
    def __init__(self, codigo, titulo, console, genero, preco):
        self.__codigo = codigo
        self.__titulo = titulo
        self.console = console
        self.genero = genero
        self.preco = float(preco)
        self.__avaliacoes = []
    @property
    def titulo(self):
        return self.__titulo

    @property
    def avaliacoes(self):
        return self.__avaliacoes
    
    @avaliacoes.setter
    def avaliacoes(self, avaliacao):
        self.__avaliacoes = avaliacao
        
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def genero(self):
        return self.__genero
    @genero.setter 
    def genero(self, valor):
        self.generos = ['Ação', 'Aventura', 'Estratégia', 'RPG', 'Esporte', 'Simulação']
        if not valor in self.generos:
            raise ValueError("Gênero inválido: {}".format(valor))
        else:
            self.__genero = valor

    @property
    def console(self):
        return self.__console
    
    @console.setter 
    def console(self, valor):
        self.consoles = ['XBox', 'PlayStation', 'Switch', 'PC']
        if not valor in self.consoles:
            raise ValueError("Console inválido: {}".format(valor))
        else:
            self.__console = valor
    

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter 
    def preco(self, valor):
        if valor <= 0 or valor>500:
            raise ValueError("Valor inválido: {}".format(valor))
        else:
            self.__preco = valor

    
class ControleJogo():       

    def __init__(self, controle_principal):        
        if not os.path.isfile("jogo.pickle"):
            self.lista_jogos = []
        else:
            with open("jogo.pickle", "rb") as f:
                self.lista_jogos = pickle.load(f)
        self.controle_principal = controle_principal

    def get_produto(self, nome):
        for produto in self.lista_jogos:
            if(produto.descricao == nome):
                return produto

    def get_jogos(self):
        return self.lista_jogos
    def cadastrar_view(self):
        self.view_cadastrar = ViewCadastraJogo(self) 

    def salvar_jogos(self):
        if len(self.lista_jogos) != 0:
            with open("jogo.pickle","wb") as f:
                pickle.dump(self.lista_jogos, f)

    def avaliar_view(self):
        self.view_cadastrar = ViewAvaliaJogo(self) 

    def consultar_view(self):
        self.view_cadastrar = ViewConsultaJogo(self) 
    def consultar(self, codigo):
        produto_encontrado = None
        for produto in self.lista_jogos:
            if(codigo == produto.codigo):
                produto_encontrado = produto 
        if(produto_encontrado is None):
            return "Produto não encontrado"
        else:
            texto = "Descrição:" + produto_encontrado.descricao +"\n"
            texto += "Valor: R$" + str(produto_encontrado.valor) + "\n"
            return texto

    def limpar_input_cadastro(self, event):
        self.view_cadastrar.input_codigo.delete(0, len(self.view_cadastrar.input_codigo.get()))
        self.view_cadastrar.input_titulo.delete(0, len(self.view_cadastrar.input_titulo.get()))
        self.view_cadastrar.input_console.delete(0, len(self.view_cadastrar.input_console.get()))
        self.view_cadastrar.input_genero.delete(0, len(self.view_cadastrar.input_genero.get()))
        self.view_cadastrar.input_preco.delete(0, len(self.view_cadastrar.input_preco.get()))

    def cadastrar(self, event):
        try: 
            codigo = self.view_cadastrar.input_codigo.get()
            titulo = self.view_cadastrar.input_titulo.get()
            console = self.view_cadastrar.input_console.get()
            genero = self.view_cadastrar.input_genero.get()
            preco = self.view_cadastrar.input_preco.get()

            jogo = Jogo(codigo, titulo, console, genero, preco)
            self.lista_jogos.append(jogo)
            self.view_cadastrar.mostrar_janela('Sucesso', 'Jogo cadastrado com sucesso')
            self.salvar_jogos()
            self.limpar_input_cadastro(event)
            self.fechar_janela_cadastrar(event)
        except ValueError as error:
            self.view_cadastrar.mostrar_janela('Erro', error) 

    def fechar_janela_cadastrar(self, event):
        self.view_cadastrar.destroy()
    def fechar_janela_avaliar(self, event):
        self.view_avaliar.destroy()
    def avaliar(self, event):
        codigo = self.view_avaliar.input_codigo.get()
        avaliacao = int(self.view_avaliar.avaliacao_feita.get().split()[0])
        jogo_encontrado =False
        for jogo in self.lista_jogos:
            if(jogo.codigo == codigo):
                jogo_encontrado =True
                jogo.avaliacoes.append(avaliacao)

        
        self.fechar_janela_avaliar(event)
        self.salvar_jogos()
        if(jogo_encontrado):
            self.view_avaliar.mostrar_janela('Sucesso', 'Jogo avaliado com sucesso')
        else:
            self.view_avaliar.mostrar_janela('Erro', 'Jogo não encontrado')
    def avaliar_view(self):
        self.view_avaliar = ViewAvaliaJogo(self) 

    def media_avaliacoes(self, array):
        return math.ceil(sum(array)/len(array))
    
    def gerar_dict_avaliacoes(self):
        dic = {str(i): [] for i in range(1,6)}

        for jogo in self.lista_jogos:
            if len(jogo.avaliacoes) == 0:
                continue 

            media = self.media_avaliacoes(jogo.avaliacoes)

            estrela = None
            if 0 <= media <= 1:
                estrela = "1"
            elif 1 < media <= 2:
                estrela = "2"
            elif 2 < media <= 3:
                estrela = "3"
            elif 3 < media <= 4:
                estrela = "4"
            elif 4 < media <= 5:
                estrela = "5"

            if estrela:
                dic[estrela].append(jogo)

        return dic

class ViewMostraProduto():
    def __init__(self, str):
        messagebox.showinfo('Produto', str)


class ViewAvaliaJogo(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.avaliacao_feita = tk.StringVar()
        self.geometry('250x250')
        self.title("Cadastro de Jogos")
        self.controle = controle


        self.frame_codigo = tk.Frame(self)
        self.frame_avaliacao = tk.Frame(self)
        self.frame_botoes = tk.Frame(self)

        self.frame_codigo.pack()
        self.frame_avaliacao.pack()
        self.frame_botoes.pack()
        

        self.label_codigo = tk.Label(self.frame_codigo,text="Código: ")
        self.label_codigo.pack(side="left")
        self.input_codigo = tk.Entry(self.frame_codigo,  width=20)
        self.input_codigo.pack(side="left")

        self.label_avaliar = tk.Label(self.frame_avaliacao,text="Avaliação: ")
        self.label_avaliar.pack(side="left")
        self.combobox = ttk.Combobox(self.frame_avaliacao, width = 15,textvariable = self.avaliacao_feita)
        self.combobox.pack(side="left")
        valores = [str(str(i) + " estrela") for i in range(1,6)]
        self.combobox['values'] = valores

        #botoes
        self.botao_enviar = tk.Button(self.frame_botoes ,text="Avaliar")      
        self.botao_enviar.pack(side="left")
        self.botao_enviar.bind("<Button>", controle.avaliar)
      
        # self.botao_limpar = tk.Button(self.frame_botoes ,text="Limpar")      
        # self.botao_limpar.pack(side="left")
        # self.botao_limpar.bind("<Button>", controle.limpar_input_cadastro)  

        self.botao_fechar = tk.Button(self.frame_botoes ,text="Sair")      
        self.botao_fechar.pack(side="left")
        self.botao_fechar.bind("<Button>", controle.fechar_janela_avaliar)
    def mostrar_janela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
class ViewCadastraJogo(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x250')
        self.title("Cadastro de Jogos")
        self.controle = controle


        self.frame_codigo = tk.Frame(self)
        self.frame_titulo = tk.Frame(self)
        self.frame_console = tk.Frame(self)
        self.frame_genero= tk.Frame(self)
        self.frame_preco= tk.Frame(self)
        self.frame_botoes = tk.Frame(self)

        self.frame_codigo.pack()
        self.frame_titulo.pack()
        self.frame_console.pack()
        self.frame_genero.pack()
        self.frame_preco.pack()
        self.frame_botoes.pack()
        

        self.label_codigo = tk.Label(self.frame_codigo,text="Código: ")
        self.label_codigo.pack(side="left")
        self.input_codigo = tk.Entry(self.frame_codigo,  width=20)
        self.input_codigo.pack(side="left")

        self.label_titulo = tk.Label(self.frame_titulo,text=" Título: ")
        self.label_titulo.pack(side="left")
        self.input_titulo = tk.Entry(self.frame_titulo,  width=20)
        self.input_titulo.pack(side="left")

        self.label_console = tk.Label(self.frame_console,text=" Console: ")
        self.label_console.pack(side="left")
        self.input_console = tk.Entry(self.frame_console,  width=20)
        self.input_console.pack(side="left")

        self.label_genero = tk.Label(self.frame_genero,text=" Gênero: ")
        self.label_genero.pack(side="left")
        self.input_genero = tk.Entry(self.frame_genero,  width=20)
        self.input_genero.pack(side="left")

        self.label_preco = tk.Label(self.frame_preco,text="Preço: R$")
        self.label_preco.pack(side="left")
        self.input_preco = tk.Entry(self.frame_preco,  width=20)
        self.input_preco.pack(side="left")

        #botoes
        self.botao_enviar = tk.Button(self.frame_botoes ,text="Cadastrar")      
        self.botao_enviar.pack(side="left")
        self.botao_enviar.bind("<Button>", controle.cadastrar)
      
        self.botao_limpar = tk.Button(self.frame_botoes ,text="Limpar")      
        self.botao_limpar.pack(side="left")
        self.botao_limpar.bind("<Button>", controle.limpar_input_cadastro)  

        self.botao_fechar = tk.Button(self.frame_botoes ,text="Sair")      
        self.botao_fechar.pack(side="left")
        self.botao_fechar.bind("<Button>", controle.fechar_janela_cadastrar)
    def mostrar_janela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class ViewConsultaJogo(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.avaliacao_selecionada = tk.StringVar()
        self.geometry('300x350')
        self.title("Consulta de Jogos")
        self.controle = controle

        self.frame_avaliacao = tk.Frame(self)
        self.frame_lista = tk.Frame(self)
        self.frame_botoes = tk.Frame(self)

        self.frame_avaliacao.pack(pady=10)
        self.frame_lista.pack()
        self.frame_botoes.pack(pady=10)

        tk.Label(self.frame_avaliacao, text="Avaliação: ").pack(side="left")
        self.combobox = ttk.Combobox(self.frame_avaliacao, width = 15, \
                                     textvariable=self.avaliacao_selecionada)
        self.combobox.pack(side="left")

        valores = [f"{i} estrela" for i in range(1,6)]
        self.combobox['values'] = valores

        self.combobox.bind("<<ComboboxSelected>>", self.atualizar_lista)

        self.listbox = tk.Listbox(self.frame_lista, width=40, height=12)
        self.listbox.pack()

        self.botao_fechar = tk.Button(self.frame_botoes, text="Sair")
        self.botao_fechar.pack()
        self.botao_fechar.bind("<Button>", controle.fechar_janela_avaliar)

    def atualizar_lista(self, event):
        self.listbox.delete(0, tk.END)

        estrela = self.avaliacao_selecionada.get().split()[0]

        dic = self.controle.gerar_dict_avaliacoes()

        jogos = dic.get(estrela, [])

        if len(jogos) == 0:
            self.listbox.insert(tk.END, "Nenhum jogo com essa avaliação.")
            return

        for jogo in jogos:
            self.listbox.insert(tk.END, f"{jogo.codigo} - {jogo.titulo} ({jogo.console})")

    def mostrar_janela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
