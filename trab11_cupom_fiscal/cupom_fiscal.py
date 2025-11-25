import tkinter as tk
import pickle
import os
from tkinter import ttk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog
import produto

class CupomFiscal:
    def __init__(self, numero):
        self.__nroCupom = numero
        self.__itensCupom = []

    @property
    def nroCupom(self):
        return self.__nroCupom

    @property
    def itensCupom(self):
        return self.__itensCupom

    def adicionar_produto(self, produto):
        for item in self.__itensCupom:
            if item["produto"] == produto:
                item["quantidade"] += 1
                return  # só retorna se achou

        # se não encontrou, adiciona
        novo_produto = {"produto": produto, "quantidade": 1}
        self.__itensCupom.append(novo_produto)




class ControleCupomFiscal:
    def __init__(self, controle_principal):
        if not os.path.isfile("cupom_fiscal.pickle"):
            self.__lista_cupons_fiscais = []
        else:
            with open("cupom_fiscal.pickle", "rb") as f:
                self.__lista_cupons_fiscais = pickle.load(f)
        self.__controle_principal = controle_principal

    def cadastrar_view(self):
        lista_produtos = self.__controle_principal.controle_produto.get_produtos()
        self.__view_cadastrar_cupom_fiscal = ViewCadastrarCupomFiscal(self, lista_produtos)

    def salvar_cupons(self):
        if len(self.__lista_cupons_fiscais) != 0:
            with open("cupom_fiscal.pickle","wb") as f:
                pickle.dump(self.__lista_cupons_fiscais, f)

    def cadastrar(self, event):
        nome_cupom_fiscal = self.__view_cadastrar_cupom_fiscal.input_numero.get()

        if nome_cupom_fiscal.strip() == "":
            messagebox.showerror("Erro", "O nome do Cupom Fiscal não pode estar vazio.")
            return

        cupom_fiscal = CupomFiscal(nome_cupom_fiscal)

        for produto in self.__view_cadastrar_cupom_fiscal.lista_produtos_selecionados:
            cupom_fiscal.adicionar_produto(produto)

        self.__lista_cupons_fiscais.append(cupom_fiscal)
        self.__view_cadastrar_cupom_fiscal.mostrar_janela("Sucesso", "Cupom Fiscal cadastrado com sucesso!")
        self.salvar_cupons()
        self.__view_cadastrar_cupom_fiscal.destroy()

    def consultar_view(self):
        numero_cupom_fiscal = simpledialog.askstring("Consultar cupom_fiscal", "Digite o numero do Cupom Fiscal:")
        if numero_cupom_fiscal is not None and numero_cupom_fiscal.strip() != "":
            cupom_fiscal = self.consultar(numero_cupom_fiscal)
            if cupom_fiscal is None:
                self.__view_mostra = ViewMostraCupomFiscal("Cupom Fiscal não encontrado.")
            else:
                str_cupom_fiscal = f"Número: {cupom_fiscal.nroCupom}\nProdutos - Quantidade:\n"
                soma = float(0)
                for produto in cupom_fiscal.itensCupom:
                    str_cupom_fiscal += f"| {produto["produto"].descricao} - {produto["quantidade"]}\n"
                    soma+= produto["quantidade"]*produto["produto"].valor
                    str_cupom_fiscal += f"| Total: - {produto["quantidade"]*produto["produto"].valor}\n\n"

                str_cupom_fiscal += f"Total: R$ {soma}\n\n"
                self.__view_mostra = ViewMostraCupomFiscal(str_cupom_fiscal)

    def consultar(self, numero):
        for cupom_fiscal in self.__lista_cupons_fiscais:
            if cupom_fiscal.nroCupom == numero:
                return cupom_fiscal
        return None


    def selecionar_produto(self, event):
        listbox = self.__view_cadastrar_cupom_fiscal.listbox_produtos_disponiveis
        
        selecionados = listbox.curselection()
        if not selecionados:
            return  # nada selecionado
        
        idx = selecionados[0]  # primeiro item selecionado
        descricao = listbox.get(idx)

        produto_selecionado = self.__controle_principal.controle_produto.get_produto(descricao)

        self.__view_cadastrar_cupom_fiscal.lista_produtos_selecionados.append(produto_selecionado)
        self.__view_cadastrar_cupom_fiscal.listbox_produtos_selecionados.insert(tk.END, descricao)


class ViewCadastrarCupomFiscal(tk.Toplevel):
    def __init__(self, controle, lista_produtos):
        tk.Toplevel.__init__(self)
        self.geometry("600x320")
        self.title("Cadastrar Cupom Fiscal")
        self.lista_produtos_disponiveis = lista_produtos
        self.lista_produtos_selecionados = []
        self.controle = controle

        self.frame_numero = tk.Frame(self)
        self.frame_listas = tk.Frame(self)
        self.frame_botoes = tk.Frame(self)

        self.frame_numero.pack()
        self.frame_listas.pack()
        self.frame_botoes.pack()

        self.label_numero = tk.Label(self.frame_numero, text="Número Cupom Fiscal:")
        self.label_numero.pack(side="left")
        self.input_numero = tk.Entry(self.frame_numero, width=25)
        self.input_numero.pack(side="left")


        self.frame_esq = tk.Frame(self.frame_listas)
        self.frame_dir = tk.Frame(self.frame_listas)
        self.frame_esq.pack(side="left", padx=10)
        self.frame_dir.pack(side="left", padx=10)

        

        self.label_produtos_disponiveis = tk.Label(self.frame_esq, text="Produtos Disponíveis:")
        self.label_produtos_disponiveis.pack()
        self.listbox_produtos_disponiveis = tk.Listbox(self.frame_esq, width=30, height=10)
        self.listbox_produtos_disponiveis.pack()
        self.listbox_produtos_disponiveis.bind("<<ListboxSelect>>", controle.selecionar_produto)

        for produto in self.lista_produtos_disponiveis:
            self.listbox_produtos_disponiveis.insert(tk.END, produto.descricao)

        self.label_produtos_selecionados = tk.Label(self.frame_dir, text="Produtos selecionados:")
        self.label_produtos_selecionados.pack()
        self.listbox_produtos_selecionados = tk.Listbox(self.frame_dir, width=30, height=10)
        self.listbox_produtos_selecionados.pack()

        self.botao_cadastrar = tk.Button(self.frame_botoes, text="Fechar Cupom")
        self.botao_cadastrar.pack(pady=5)
        self.botao_cadastrar.bind("<Button>", controle.cadastrar)

    def mostrar_janela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class ViewMostraCupomFiscal:
    def __init__(self, str_msg):
        messagebox.showinfo("Cupom Fiscal", str_msg)
